<template>
  <div id="photos_soil_drill_print_page">

    <div id="eee" v-show="!ifShowLoadingNowFlag">

      <div id="tableMainTitleContainer">
        {{soilDrillTableTitle}}的照片汇总页
      </div>

      <div id="headerTableContainer">
        <Table ref="headerTable" border :width="tableRealWidth" :style="'left:'+tableLeftEdge+'px;'"
               :columns="table_view_column_arr"
               :data="table_view_data_arr"
               class="photosTitleTable"
               :disabled-hover = true
               :row-class-name = "customPhotoHeaderTableRowContentNormalStyle">
        </Table>
      </div>

      <div id="photoesTableContainer" v-show="photos_data_arr.length>0">
        <Table ref="photosTable" border :width="tableRealWidth" :style="'left:'+tableLeftEdge+'px;'"
               :columns="photos_column_arr"
               :data="photos_data_arr"
               :show-header = false
               :disabled-hover = true
               :row-class-name = "customPhotoTableRowStyle"
        ></Table>
      </div>

      <p>&nbsp;</p>

    </div>

    <Card shadow :style="'background-color:#eeeeee;z-index:1001;width:'+imgShowContainerRealWidth+'px;height:'+imgShowContainerRealHeight+'px;position:fixed;top:50px;left:'+imgShowContainerEdgeW+'px;'" v-show="ifShowImageFlag">
      <div style="position:relative;">
        <span class="u-imgBasicInfo" v-show="imgSelfShowFlag">图片文件名：{{currentShowImageFileName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{currentShowImageDateTime}}</span>
        <span class="u-imgCloseBtn"><Button type="primary" @click="closeImageShow">关闭图片显示</Button></span>
      </div>
      <hr>
      <div v-show="imgSelfShowFlag" style="position:relative;clear:both;text-align:center;width:auto;">
        <img id="imgEntity" :src="currentShowImageURL" :width="imageRealShowWidth" :height="imageRealShowHeight">
      </div>
      <div v-show="imgSelfShowFlag" style="margin-top:10px;font-size:16px;font-weight:bold">
        <span>{{currentShowImageComment}}</span>
      </div>

      <div v-show="!imgSelfShowFlag" style="margin-top:20px;font-size:16px">
        <span>图片正在加载中，请稍候......</span>
      </div>
    </Card>

    <div class="zhezhao" id="zhezhao"></div>

    <circleLoading id="loadingEntityForViewSoilDrillRecord" v-show="ifShowLoadingNowFlag"></circleLoading>

  </div>
</template>

<script>
  export default
  {
    name: "photos_soil_drill_page",
    data() {
      return {
        ifShowImageFlag:false,
        imgShowContainerEdgeW:'',
        imgShowContainerRealWidth:960,
        imgShowContainerRealHeight:750,
        imgSelfShowFlag:false,
        imageRealShowWidth:'',
        imageRealShowHeight:'',
        currentShowImageFileName:'',
        currentShowImageDateTime:'',
        currentShowImageComment:'',
        currentShowImageURL:'',

        soilDrillTableTitle:'',
        table_view_column_arr:[],
        table_view_data_arr:[],
        photos_column_arr:[],
        photos_data_arr:[],
        tableLeftEdge:'',
        tableRealWidth:772,
        ifShowLoadingNowFlag:true,
        arr_photo_filepath:[],
        arr_photo_width_height:[],
        current_photos_collection:{

        },
        imagesPlaceHolderObj:{
          h_0_left:'/static/empty.png',
          h_0_right:'/static/empty.png',
          h_2_left:'/static/empty.png',
          h_2_right:'/static/empty.png',
          h_4_left:'/static/empty.png',
          h_4_right:'/static/empty.png',
          h_6_left:'/static/empty.png',
          h_6_right:'/static/empty.png',
        }
      }
    },

    mounted: function ()
    {
      window.scrollTo(0, 0);

      this.currentRecordId = Number(this.$route.params.id);

      this.initHeaderTableColumns();

      this.getRealRecordFromDataBase();

      this.rearrangeUIAfterResizeShowArea();
    },

    methods:
    {

      openViewOneImage(imageURL){



        this.currentShowImageURL = imageURL;

        this.imgSelfShowFlag = false;

        this.ifShowImageFlag = true;

        for(var i=0;i<this.arr_photo_filepath.length;i++)
        {
          if(this.arr_photo_filepath[i] == imageURL){
            let arr = this.arr_photo_filepath[i].split("/");
            this.currentShowImageFileName = arr[arr.length-1];
            this.currentShowImageComment = this.arr_photo_comment[i];
            this.currentShowImageDateTime = "(上传时间："+this.arr_photo_datetime[i]+")";
          }
        }

        this.imgObj = new Image();
        this.imgObj.src = imageURL;
        this.imgObj.onload = this.getImageLoadedHandler

        this.d("zhezhao").style.display = 'block';
        this.d("zhezhao").style.height = document.body.scrollHeight + "px";

        setTimeout(()=>{
          this.d("zhezhao").style.height = (document.body.scrollHeight+60) + "px";
        },10)
      },

      getImageLoadedHandler() {

        let aw = this.imgObj.width;
        let ah = this.imgObj.height;
        let bh,bw;
        if(aw>ah)
        {
          bw = this.imgShowContainerRealWidth - 100;
          bh = Math.floor(ah * bw / aw);
          while(bh>this.imgShowContainerRealHeight - 90)
          {
            bh*=0.9;
            bw*=0.9
          }
        }else{
          bh = this.imgShowContainerRealHeight - 105;
          bw = Math.floor(aw * bh / ah);
        }
        this.imgObj.width = bw;
        this.imgObj.height = bh;
        this.imageRealShowWidth = bw;
        this.imageRealShowHeight = bh;
        this.imgSelfShowFlag = true;
      },


      closeImageShow(){
        this.d("zhezhao").style.display = 'none';
        this.ifShowImageFlag = false;
        //setTimeout(this.setScrollToBottom,10);
      },

      setScrollToBottom(){
        document.body.scrollTop = document.body.scrollHeight;
        window.scrollTo(0, document.body.scrollHeight);
      },

      initHeaderTableColumns()
      {
        this.table_view_column_arr = [];

        let a = [
          {
            title: '东经（° ）',
            key: 'dongjing',
            align: 'center',
            width: 150,
          },
          {
            title: '北纬（° ）',
            key: 'beiwei',
            align: 'center',
            width: 150,
          }];


        this.table_view_column_arr = [];
        this.table_view_column_arr[0]={title:'点位编号',key:'dianwei',width:150,align: 'center'};
        this.table_view_column_arr[1]={title:'采样点位坐标',key:'caiyangdianweizuobiao',width:300,align: 'center',
          children:a};
        this.table_view_column_arr[2]={title:'钻探方式',key:'zuantanfangshi',width:150,align: 'center'};
        this.table_view_column_arr[3]={title:'采集样品种类',key:'caijiyangpinzhonglei',width:170,align: 'center'};

        this.photos_column_arr = [];

        this.photos_column_arr[0]={title:'左边照片',key:'leftPhoto',width:385,align: 'center',
          render:(h,params)=>{

            if(params.row.leftPhoto.indexOf("/")>-1)
            {
              let goodWH_arr = this.calcRealImgShouldBeShowdWidthAndHeight(params.index,"left");
              // width:this.calcRealImgShouldBeShowdWidth(params.index,"left"),
              //   height:this.calcRealImgShouldBeShowdHeight(params.index,"left"),

              return h('div', {
                  on: {
                    'click': (e) => {
                      if(this.imagesPlaceHolderObj["h_" + params.index + "_left"].indexOf("/static/empty.png") == -1)
                      {
                        this.openViewOneImage(this.imagesPlaceHolderObj["h_" + params.index + "_left"]);
                      }
                    }
                  },
                  domProps: {
                    title:
                      this.imagesPlaceHolderObj["h_"+params.index+"_left"].indexOf("/static/empty.png")==-1?"点击显示大图":""
                  },
                  style:{
                    cursor:this.imagesPlaceHolderObj["h_"+params.index+"_left"].indexOf("/static/empty.png")==-1?"pointer":"arrow"
                  }
                },
                [
                  h('img', {
                    domProps: {
                      src: this.imagesPlaceHolderObj["h_"+params.index+"_left"],
                    },
                    style:{
                      verticalAlign:'middle',
                      width:goodWH_arr[0],
                      height:goodWH_arr[1],

                    }
                  })
                ]
              )
            }else{

              return h('div',
                {
                  on: {
                    'click': (e) => {
                      //alert("点击选择相应图片");
                      this.sumulateGetOnePic(params.index+"_left");
                    }
                  },
                  style:{
                    cursor:"pointer"
                  }
                },
                [
                  h('span', {
                    domProps: {
                      innerHTML: params.row.leftPhoto,
                      title:'点击选择照片'
                    },
                    style:{
                      color:"#000000",
                      fontFamily:"Microsoft YaHei",
                      fontSize:"15px",
                      fontWeight:"bold"
                    },
                })
              ])
            }
          }
        };

        this.photos_column_arr[1]={title:'右边照片',key:'rightPhoto',width:385,align: 'center',
          render:(h,params)=>{

          if(params.row.rightPhoto.indexOf("/")>-1)
          {
            let goodWH_arr = this.calcRealImgShouldBeShowdWidthAndHeight(params.index,"right");
            // width:this.calcRealImgShouldBeShowdWidth(params.index,"right"),
            //   height:this.calcRealImgShouldBeShowdHeight(params.index,"right"),

            return h('div', {
                on: {
                  'click': (e) => {
                      if(this.imagesPlaceHolderObj["h_"+params.index+"_right"].indexOf("/static/empty.png")==-1){
                          this.openViewOneImage(this.imagesPlaceHolderObj["h_" + params.index + "_right"]);
                      }
                  },
                },
                domProps: {
                  title: this.imagesPlaceHolderObj["h_"+params.index+"_right"].indexOf("/static/empty.png")==-1?"点击显示大图":""
                },
                style:{
                  cursor:this.imagesPlaceHolderObj["h_"+params.index+"_right"].indexOf("/static/empty.png")==-1?"pointer":"arrow"
                }
              },
              [
                h('img', {
                  domProps: {
                    src: this.imagesPlaceHolderObj["h_"+params.index+"_right"],
                  },
                  style:{
                    verticalAlign:'middle',
                    width:goodWH_arr[0],
                    height:goodWH_arr[1],
                  }
                })
              ]
            )
          }else{

            return h('div',
              {
                on: {
                  'click': (e) => {
                      //alert("点击选择相应图片");
                      this.sumulateGetOnePic(params.index+"_right");
                  }
                },
                style:{
                  cursor:"pointer"
                }
              },
              [
                h('span', {
                    domProps: {
                      innerHTML: params.row.rightPhoto,
                      title:'点击选择照片'
                    },
                    style:{
                      color:"#000000",
                      fontFamily:"Microsoft YaHei",
                      fontSize:"15px",
                      fontWeight:"bold"
                    },

                  })
                ])
            }
          }
        };

        this.photos_data_arr = [];
        this.photos_data_arr[0]={leftPhoto:"",rightPhoto:""};
        this.photos_data_arr[1]={leftPhoto:"钻探前照片",rightPhoto:"钻探后照片"};
        this.photos_data_arr[2]={leftPhoto:"",rightPhoto:""};
        this.photos_data_arr[3]={leftPhoto:"东",rightPhoto:"南"};
        this.photos_data_arr[4]={leftPhoto:"",rightPhoto:""};
        this.photos_data_arr[5]={leftPhoto:"西",rightPhoto:"北"};
        this.photos_data_arr[6]={leftPhoto:"",rightPhoto:""};
        this.photos_data_arr[7]={leftPhoto:"采样前照片",rightPhoto:"采样后照片"};

        for(var i=0;i<this.photos_data_arr.length;i++)
        {
          if(i%2==0)
          {
            this.photos_data_arr[i].leftPhoto = this.imagesPlaceHolderObj["h_"+i+"_left"];
            this.photos_data_arr[i].rightPhoto = this.imagesPlaceHolderObj["h_"+i+"_right"];
          }
        }

      },

      //marginLeft:'-18px',

      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent()
      {
        this.rearrangeUIAfterResizeShowArea();
      },


      calcRealImgShouldBeShowdWidthAndHeight(index,dirc){
        if(this.imagesPlaceHolderObj["h_"+index+"_"+dirc] == '/static/empty.png'){
          return ['200px','30px'];
        }
        let aw,ah,bw,bh;
        for(var i=0;i<this.arr_photo_filepath.length;i++)
        {
          if(this.arr_photo_filepath[i] == this.imagesPlaceHolderObj["h_"+index+"_"+dirc]){
            aw = this.arr_photo_width_height[i][0];
            ah = this.arr_photo_width_height[i][1];
          }
        }

        if(aw>ah)
        {
          bw = 385 - 30;
          bh = Math.floor(ah * bw / aw);
          while(bh>250)
          {
            bh*=0.9;
            bw*=0.9
          }
        }else{
          bh = 250;
          bw = Math.floor(aw * bh / ah);
        }
        return [bw+"px",bh+"px"];
      },

      calcRealImgShouldBeShowdWidth(index,dirc)
      {
        if(this.imagesPlaceHolderObj["h_"+index+"_"+dirc] == '/static/empty.png'){
          return '200px';
        }
        let w,h;
        for(var i=0;i<this.arr_photo_filepath.length;i++)
        {
          if(this.arr_photo_filepath[i] == this.imagesPlaceHolderObj["h_"+index+"_"+dirc]){
            w = this.arr_photo_width_height[i][0];
            h = this.arr_photo_width_height[i][1];
          }
        }

        let rew = w*250/h - 30
        // if(rew > 385)
        // {
        //   rew = 385 - 30;
        // }
        return rew + "px";
      },

      calcRealImgShouldBeShowdHeight(index,dirc)
      {
        if(this.imagesPlaceHolderObj["h_"+index+"_"+dirc] == '/static/empty.png'){
          return '30px';
        } else {
          return '250px';
        }
      },

      sumulateGetOnePic(lockIndex){

        let ri = Number(lockIndex.split("_")[0]) - 1;
        let postfix = lockIndex.split("_")[1];

        if(postfix == "left"){
          this.imagesPlaceHolderObj["h_"+ri+"_"+postfix] = this.arr_photo_filepath[ri];
        }else{
          this.imagesPlaceHolderObj["h_"+ri+"_"+postfix] = this.arr_photo_filepath[ri+1];
        }

      },


      getRealRecordFromDataBase(){
        let params = new URLSearchParams();

        params.append('record_id', this.currentRecordId);

        this.axios({
          method: 'post',
          url: 'http://huankepy.neuseer.cn/select_pointed_soil_drill_record',
          data: params
        }).then((result) => {

          console.log(result.data.result)

          let tableFieldsArr = this.$store.state.soil_drill_record_table_fields;

          let res = JSON.parse(result.data.result);

          this.dianwei_number = res[0][tableFieldsArr.indexOf('dianwei_number')];

          this.jingdu = res[0][tableFieldsArr.indexOf('jingdu')];
          this.weidu = res[0][tableFieldsArr.indexOf('weidu')];
          this.drill_method = res[0][tableFieldsArr.indexOf('drill_method')];
          this.sample_type = '土壤';

          this.soilDrillTableTitle = res[0][tableFieldsArr.indexOf('record_table_name')];
          this.arr_photo_filepath = res[0][tableFieldsArr.indexOf('arr_photo_filepath')].split("**");
          this.arr_photo_comment = res[0][tableFieldsArr.indexOf('arr_photo_comment')].split("**");
          this.arr_photo_datetime = res[0][tableFieldsArr.indexOf('arr_photo_datetime')].split("**");
          this.arr_photo_width_height	 = JSON.parse(res[0][tableFieldsArr.indexOf('arr_photo_width_height')]);
          this.current_photos_collection = JSON.parse(res[0][tableFieldsArr.indexOf('photos_collection')]);

          this.table_view_data_arr = [];

          this.table_view_data_arr.push({dianwei:this.dianwei_number,dongjing:this.jingdu,beiwei:this.weidu,zuantanfangshi:this.drill_method,caijiyangpinzhonglei:this.sample_type});

          this.ifShowLoadingNowFlag = false;

        });
      },

      rearrangeUIAfterResizeShowArea()
      {
        this.tableLeftEdge = (document.body.offsetWidth - this.tableRealWidth) /2;

        this.imgShowContainerEdgeW = (document.body.offsetWidth - this.imgShowContainerRealWidth)/2;

        this.imgShowContainerRealHeight = document.documentElement.clientHeight - 61;

        if(this.d("loadingEntityForViewSoilDrillRecord") != null)
        {
          this.d("loadingEntityForViewSoilDrillRecord").style.left = (document.body.offsetWidth - this.d("loadingEntityForViewSoilDrillRecord").offsetWidth) / 2 + "px";

        }
      },

      customPhotoHeaderTableRowContentNormalStyle (row, index) {

        // 表示所有表格内容行，都应用统一的样式
        return 'photoHeaderTableRow';
      },

      customPhotoTableRowStyle (row, index) {

        if(index%2==1)
        {
          return 'photoTableOddNumberRow';
        } else {
          return 'photoTableEvenNumberRow'
        }
      },

      updateSoilDrillTable()
      {
        let params = new URLSearchParams();

        let operateTableActionStr = '/update_parts_for_soil_drill_table';

        params.append('record_id', this.currentRecordId);
        params.append('photos_collection', JSON.stringify(this.current_photos_collection));

          this.axios({

            method: 'post',
            url: 'http://huankepy.neuseer.cn' + operateTableActionStr,
            data: params

          }).then((res) => {


          }).catch((error) => {
            alert("更新数据表失败");
            console.log("update data to mysql error: " + error)
          });

      },


    }

  }
</script>

<style>
  .photosTitleTable .ivu-table-header tr {
    font-size:14px;
    font-weight:bold;
  }
  .photosTitleTable .ivu-table-header td {
    height:22px;
  }

  .ivu-table .photoHeaderTableRow td{
    color: #136BBD;
    font-size:14px;
  }

  .ivu-table .photoTableOddNumberRow td{
    /*background: #f8ffc2;*/
    background:rgba(248,255,194,0.3);
    height:30px;
  }

  .ivu-table .photoTableEvenNumberRow td{
    text-align:center;
  }

</style>

<style scoped>

  #tableMainTitleContainer{
    width: 100%;
    text-align: center;
    margin-top: 60px;
    margin-bottom: 10px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #viceTitle{
    text-align: center;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #loadingEntityForViewSoilDrillRecord{
    position:fixed;
    top:190px;
  }

  #headerTableContainer{
    margin-top:35px;
  }

  .u-imgBasicInfo{
    float:left;
    margin-left:20px;
    margin-top:0;
    margin-bottom:15px;
    font-size:16px;
  }

  .u-imgCloseBtn{
    float:right;
    margin-right:15px;
    margin-top:-5px;
    cursor:pointer;
  }

  .photoTitleStyInTable{
    font-weight:bold;
    font-size:18px;
    color:#ff00ff
  }

  .zhezhao
  {
    width:100%;
    height:100%;
    background-color:#000;
    filter:alpha(opacity=50);
    -moz-opacity:0.5;
    opacity:0.5;
    position:absolute;
    left:0px;
    top:0px;
    display:none;
    z-index:997;
  }

</style>

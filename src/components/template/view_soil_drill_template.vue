<template>
    <div id="view_soil_drill_template">

      <Breadcrumb style="text-align: left; margin-left:100px;margin-bottom:-40px;" separator=">"
                  v-show="!ifShowImageFlag">
        <BreadcrumbItem to="/">首页</BreadcrumbItem>
        <BreadcrumbItem to="/soil_entrance">土壤类记录表</BreadcrumbItem>
        <BreadcrumbItem to="/soil_list/0">电子土壤钻孔记录表</BreadcrumbItem>
        <BreadcrumbItem to="/template/list/soil_drill_template_list/0">模板列表</BreadcrumbItem>
        <BreadcrumbItem>查看已有模板</BreadcrumbItem>
      </Breadcrumb>

      <div id="newTableTitleHint">
        {{template_table_name}}
      </div>

      <div id="fillContentLayer" v-show="!ifShowImageFlag && !ifShowLoadingNowFlag">

        <hr style="margin-top:30px;height:1px;border:none;border-top:1px dashed gray;"/>

          <div class="m-smallTitle">1、基本信息</div>

          <div class="m-sonItem"><span class="m-span-label">地块名称：</span>

            <span class="m-realFieldValue">{{dikuai_name}}
            </span>
            <span class="m-hp-center">&nbsp;</span>
            <span class="m-span-label">地块编码：</span>
            <span class="m-realFieldValue">{{dikuai_code}}
            </span>
          </div>

          <div class="m-sonItem"><span class="m-span-label">布点人员：</span>

            <span class="m-realFieldValue">{{budian_person}}
            </span>
            <span class="m-hp-center">&nbsp;</span>
            <span class="m-span-label">布点日期：</span>
            <span class="m-realFieldValue">{{budian_date}}
            </span>
          </div>

        <div class="m-smallTitle">2、点位信息</div>

        <div class="m-sonItem"><span class="m-span-label">采样日期：</span>

          <span class="m-realFieldValue">{{caiyang_date}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">采样人员：</span>
          <span class="m-realFieldValue">{{caiyang_person}}</span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">天气：</span>

          <span class="m-realFieldValue">{{weather_info}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">点位编号：</span>
          <span class="m-realFieldValue">{{dianwei_number}}</span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">经度：</span>

          <span class="m-realFieldValue">{{jingdu}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">纬度：</span>
          <span class="m-realFieldValue">{{weidu}}</span>
        </div>

        <div class="m-single"><span class="m-span-label">采样地点：</span>

          <span class="m-realFieldValue">{{caiyang_site}}</span>

        </div>

        <div class="m-smallTitle">3、钻孔信息</div>

        <div class="m-sonItem"><span class="m-span-label">钻孔负责人：</span>

          <span class="m-realFieldValue">{{drill_person_name}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">联系方式：</span>
          <span class="m-realFieldValue">{{drill_person_contact}}
            </span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">钻孔深度(m)：</span>

          <span class="m-realFieldValue">{{drill_depth}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">钻孔直径(mm)：</span>
          <span class="m-realFieldValue">{{drill_diameter}}</span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">钻孔方法：</span>

          <span class="m-realFieldValue">{{drill_method}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">钻机型号：</span>
          <span class="m-realFieldValue">{{drill_machine_model}}</span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">初见水位(m)：</span>

          <span class="m-realFieldValue">{{chujian_water_level}}</span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">止孔深度(m)：</span>
          <span class="m-realFieldValue">{{zhikong_depth}}</span>
        </div>

        <div class="m-smallTitle">4、钻进操作记录</div>

        <div id="drillOperatetemplateList" v-show="!ifShowLoadingNowFlag && table_view_data_arr.length>0">
          <Table :row-class-name = "customTableRowContentNormalStyle" size="large" ref="operatetemplateTable" border :width="tableViewRealWidth" :style="'left:'+tableViewLeftEdge+'px;'"
                 :columns="table_view_column_arr"
                 :data="table_view_data_arr"
                 disabled-hover>
          </Table>
        </div>


        <div class="m-placeholder">&nbsp;&nbsp;</div>

        <hr style="position:relative;margin-bottom:20px;height:2px;border:none;border-top:1px dashed gray;"/>

          <div class="m-single-line"><span class="m-span-label-long">钻孔负责人：</span>

            <span class="m-realFieldValue">{{drill_person_name}}</span>

          </div>
          <br>
          <div class="m-single-line"><span class="m-span-label-long">记录人：</span>

            <span class="m-realFieldValue">{{record_person_name}}</span>

          </div>
          <br>
          <div class="m-single-line"><span class="m-span-label-long">采样单位的内审签名：</span>

            <span class="m-realFieldValue">{{neishen_signature}}</span>

          </div>
        <br>
        <br>
        <br>
        <br>
        <div id="currentFillInStatusHintContainer" style="margin-top:15px">
        <Button type="primary" size="large" @click="readyForEditAgain">点击重新编辑</Button>
        </div>
        <br>
        <br>
        <br>

        <br>
        <br>
        <br>
      </div>


      <circleLoading id="loadingEntityForViewSoilDrillTemplate" v-show="ifShowLoadingNowFlag"></circleLoading>

    </div>
</template>

<script>
  export default
  {

    name: "view_soil_drill_template",

    data() {
      return {
        table_data_arr:[],
        table_column_arr:[],
        ifShowLoadingNowFlag:true,
        currentTemplateId:'',
        ifShowImageFlag:false,
        openTheDatePickPanelFlag:false,
        table_view_column_arr: [],
        table_view_data_arr: [],
        tableViewLeftEdge:0,
        tableViewRealWidth:743,
        tableForPDFViewRealWidth:744,
        selectedDateForFillTable:'',
        dikuai_name:'',
        dikuai_code:'',
        budian_person:'',
        budian_date:'',
        caiyang_date:'',
        caiyang_person:'',
        weather_info:'',
        dianwei_number:'',
        jingdu:'',
        weidu:'',
        caiyang_site:'',
        drill_person_name:'',
        drill_person_contact:'',
        drill_depth:'',
        drill_method:'',
        drill_diameter:'',
        drill_machine_model:'',
        chujian_water_level:'',
        zhikong_depth:'',
        record_person_name:'',
        neishen_signature:'',
        arr_sample_number:[],
        arr_zuanjin_depth:[],
        arr_diceng_describe:[],
        arr_wuran_describe:[],
        arr_caiyang_depth:[],
        arr_photo_filepath:[],
        arr_photo_comment:[],
        arr_photo_datetime:[],
        alreadyUploadedImagesList:[],
        ifShowImageFlag:false,
        imgShowContainerEdgeW:'',
        imgShowContainerRealWidth:960,
        imageRealShowWidth:'',
        imageRealShowHeight:'',
        currentShowImageURL:"",
        currentShowImageFileName:'',
        currentShowImageDateTime:'(照片拍摄时间：2018-07-15 09:26)',
        currentShowImageComment:'',
        imgShowContainerRealHeight:750,
        imgSelfShowFlag:false,
        ifDeleteOneImageHintFlag:false,
        currentShowImageIndex:-1,
        template_table_name:'',
        template_date:'',
        table_view_column_arr_pdf:[],
        pdfFileName:'',
        ifExportPDFFileFlag:false
      }
    },

    mounted: function ()
    {

      document.body.scrollTop = 0;

      window.scrollTo(0, 0);

      this.currentTemplateId = Number(this.$route.params.id);

      //console.log("this.currentTemplateId=="+this.currentTemplateId);

      //this.currentTemplateId = 1

      //$route为当前router跳转的对象，可以获取name、path、query、params等

      //$router为VueRouter实例，想要导航到不同URL，则使用$router.push方法

      //返回上一个history也是使用$router.go方法

      this.getPointedSoilDrillTemplate();

      this.rearrangeUIAfterResizeShowArea();


    },
    methods:{

      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      },

      customTableRowContentStyleForPDF (row, index) {

        return 'm-table-row-pdf-style';
      },

      customTableRowContentNormalStyle (row, index) {

        return 'm-table-row-style';
      },

      initReadyOK()
      {
        this.ifShowLoadingNowFlag = false;
        this.rearrangeUIAfterResizeShowArea();
      },

      getPointedSoilDrillTemplate(){

        let params = new URLSearchParams();

        params.append('template_id', this.currentTemplateId);

        this.axios({
          method: 'post',
          url: 'http://huankepy.neuseer.cn/select_pointed_soil_drill_template',
          data: params
        }).then((result) => {

          let a = [
            {
              title: '（m）',
              key: 'zuanjin_depth',
              align: 'center',
              width: 100,
            }];

          let b = [
                {
                  title: '土质分类、密度、颜色、湿度',
                  key: 'diceng_describe',
                  align: 'center',
                  width: 220,
                }];

          let c=[
                {
                  title: '气味、污染痕迹、油状物等',
                  key: 'wuran_describe',
                  align: 'center',
                  width: 220
                }];

          let d=[
            {
              title: '（m）',
              key: 'caiyang_depth',
              align: 'center',
              width: 100
            }];

          this.table_view_column_arr = [];
          this.table_view_column_arr[0]={title:'样品编号',key:'sample_number',width:100,align: 'center'};
          this.table_view_column_arr[1]={title:'钻进深度',key:'zuanjin_depth',width:100,align: 'center', children:a};
          this.table_view_column_arr[2]={title:'地层描述',key:'diceng_describe',width:220,align: 'center', children:b};
          this.table_view_column_arr[3]={title:'污染描述',key:'wuran_describe',width:220,align: 'center', children:c};
          this.table_view_column_arr[4]={title:'采样深度',key:'caiyang_depth',width:100,align: 'center', children:d};

          this.table_view_column_arr_pdf = [];
          this.table_view_column_arr_pdf[0]={title:'样品编号',key:'sample_number',width:100,align: 'center'};
          this.table_view_column_arr_pdf[1]={title:'钻进深度',key:'zuanjin_depth',width:100,align: 'center', children:a};
          this.table_view_column_arr_pdf[2]={title:'地层描述',key:'diceng_describe',width:220,align: 'center', children:b};
          this.table_view_column_arr_pdf[3]={title:'污染描述',key:'wuran_describe',width:220,align: 'center', children:c};
          this.table_view_column_arr_pdf[4]={title:'采样深度',key:'caiyang_depth',width:100,align: 'center', children:d};


          let tableFieldsArr = this.$store.state.soil_drill_template_table_fields;

          //console.log("result.data.result=="+result.data.result);

          let res = JSON.parse(result.data.result);

          this.template_table_name = res[0][tableFieldsArr.indexOf('template_table_name')];

          this.record_person_name = res[0][tableFieldsArr.indexOf('record_person_name')];

          this.neishen_signature = res[0][tableFieldsArr.indexOf('neishen_signature')];

        console.log("this.neishen_signature=="+this.neishen_signature);

          this.dikuai_name = res[0][tableFieldsArr.indexOf('dikuai_name')];


        console.log("this.dikuai_name=="+this.dikuai_name);

          this.dikuai_code = res[0][tableFieldsArr.indexOf('dikuai_code')];
        console.log("this.dikuai_code=="+this.dikuai_code);

          this.budian_person = res[0][tableFieldsArr.indexOf('budian_person')];

        console.log("this.budian_person=="+this.budian_person);

          this.budian_date = res[0][tableFieldsArr.indexOf('budian_date')];

        console.log("this.budian_date=="+this.budian_date);

          this.caiyang_date = res[0][tableFieldsArr.indexOf('caiyang_date')];

        console.log("this.caiyang_date=="+this.caiyang_date);

          this.caiyang_person = res[0][tableFieldsArr.indexOf('caiyang_person')];

        console.log("this.caiyang_person=="+this.caiyang_person);

          this.weather_info = res[0][tableFieldsArr.indexOf('weather_info')];

        console.log("this.weather_info=="+this.weather_info);

          this.dianwei_number = res[0][tableFieldsArr.indexOf('dianwei_number')];

        console.log("this.dianwei_number=="+this.dianwei_number);

          this.jingdu = res[0][tableFieldsArr.indexOf('jingdu')];

        console.log("this.jingdu=="+this.jingdu);

        this.weidu = res[0][tableFieldsArr.indexOf('weidu')];

        console.log("this.weidu=="+this.weidu);

          this.caiyang_site = res[0][tableFieldsArr.indexOf('caiyang_site')];

        console.log("this.caiyang_site=="+this.caiyang_site);

          this.drill_person_name = res[0][tableFieldsArr.indexOf('drill_person_name')];

        console.log("this.drill_person_name=="+this.drill_person_name);

          this.drill_person_contact = res[0][tableFieldsArr.indexOf('drill_person_contact')];

        console.log("this.drill_person_contact=="+this.drill_person_contact);

          this.drill_depth = res[0][tableFieldsArr.indexOf('drill_depth')]

          console.log("this.drill_depth=="+this.drill_depth);

          this.drill_diameter = res[0][tableFieldsArr.indexOf('drill_diameter')];

          console.log("this.drill_diameter=="+this.drill_diameter);

          this.drill_method = res[0][tableFieldsArr.indexOf('drill_method')];

          console.log("this.drill_method=="+this.drill_method);

          this.drill_machine_model = res[0][tableFieldsArr.indexOf('drill_machine_model')];

          console.log("this.drill_machine_model=="+this.drill_machine_model);

          this.chujian_water_level = res[0][tableFieldsArr.indexOf('chujian_water_level')];

          console.log("this.chujian_water_level=="+this.chujian_water_level);

          this.zhikong_depth = res[0][tableFieldsArr.indexOf('zhikong_depth')];

          console.log("this.zhikong_depth=="+this.zhikong_depth);

          // if(res[0][tableFieldsArr.indexOf('arr_sample_number')].indexOf("**")>-1)
          // {
          //   this.arr_sample_number = res[0][tableFieldsArr.indexOf('arr_sample_number')].split("**");
          // }
          this.arr_sample_number = res[0][tableFieldsArr.indexOf('arr_sample_number')].split("**");

          // if(res[0][tableFieldsArr.indexOf('arr_zuanjin_depth')].indexOf("**")>-1)
          // {
          //   this.arr_zuanjin_depth = res[0][tableFieldsArr.indexOf('arr_zuanjin_depth')].split("**");
          // }

          this.arr_zuanjin_depth = res[0][tableFieldsArr.indexOf('arr_zuanjin_depth')].split("**");

          // if(res[0][tableFieldsArr.indexOf('arr_diceng_describe')].indexOf("**")>-1)
          // {
          //   this.arr_diceng_describe = res[0][tableFieldsArr.indexOf('arr_diceng_describe')].split("**");
          // }

        this.arr_diceng_describe = res[0][tableFieldsArr.indexOf('arr_diceng_describe')].split("**");

          // if(res[0][tableFieldsArr.indexOf('arr_wuran_describe')].indexOf("**")>-1)
          // {
          //   this.arr_wuran_describe = res[0][tableFieldsArr.indexOf('arr_wuran_describe')].split("**");
          // }

        this.arr_wuran_describe = res[0][tableFieldsArr.indexOf('arr_wuran_describe')].split("**");

          // if(res[0][tableFieldsArr.indexOf('arr_caiyang_depth')].indexOf("**")>-1)
          // {
          //   this.arr_caiyang_depth = res[0][tableFieldsArr.indexOf('arr_caiyang_depth')].split("**");
          // }

        this.arr_caiyang_depth = res[0][tableFieldsArr.indexOf('arr_caiyang_depth')].split("**");



          var i;

          this.table_view_data_arr = [];

          for(i=0;i<this.arr_sample_number.length;i++)
          {
            this.table_view_data_arr.push({sample_number:this.arr_sample_number[i],zuanjin_depth:this.arr_zuanjin_depth[i],diceng_describe:this.arr_diceng_describe[i],wuran_describe:this.arr_wuran_describe[i],caiyang_depth:this.arr_caiyang_depth[i],})
          }



          this.initReadyOK();

        })
      },


      setScrollToBottom(){
        document.body.scrollTop = document.body.scrollHeight;
        window.scrollTo(0, document.body.scrollHeight);
      },

      rearrangeUIAfterResizeShowArea() {

        this.tableViewLeftEdge = (760 - this.tableViewRealWidth) /2;

        this.imgShowContainerEdgeW = (document.body.offsetWidth - this.imgShowContainerRealWidth)/2;

        this.imgShowContainerRealHeight = document.documentElement.clientHeight - 61;

        this.d("loadingEntityForViewSoilDrillTemplate").style.left = (document.body.offsetWidth - this.d("loadingEntityForViewSoilDrillTemplate").offsetWidth) / 2 + "px";

      },

      readyForEditAgain(){
        this.$router.push(`/template/compile_soil_drill_template/${this.currentTemplateId}`)
      },
    }
  }
</script>

<style scoped>

  #fillContentLayer {
    position: relative;
    width: 760px;
    height: auto;
    margin: auto;
  }

  #pdfDom{
    width:780px;
    text-align:center;
    padding-left:10px;
    padding-right:10px;
    display:none;
  }

  #loadingEntityForViewSoilDrillTemplate{
    position:fixed;
    top:190px;
  }

  .u-imgBasicInfo{
    float:left;
    margin-left:20px;
    margin-top:0;
    margin-bottom:15px;
    font-size:16px;
  }

  .m-input-template-name-box {
    margin: 0 auto;
  }

  .u-imgCloseBtn{
    float:right;
    margin-right:15px;
    margin-top:-5px;
    cursor:pointer;
  }

  .m-realFieldValue{
    position:relative;
    width:200px;
    height:15px;
    line-height:15px;
    text-align:left;
    display:inline-block;
    color: #136BBD;
    font-size:14px;
  }

  .m-only-for-pdf{
    font-weight:bold;
    font-size:14px;
    color: #000000;
  }

  .m-inscribe-date{
    position:relative;
    float:right;
    margin-right:15px;
    font-size:14px;
  }

  .m-smallTitle {
    clear:both;
    padding: 20px;
    padding-top: 20px;
    text-align: left;
    font-size: 16px;
    font-weight: bold;
  }

  .m-picList{
    position:relative;
    margin-top:20px;
    margin-bottom:-10px;
  }

  .m-picSingleInfoLine{
    position:relative;
    display:block;
    height:auto;
  }

  .m-picfilename{
    position:relative;
    clear:both;
    float:left;
    margin-left:20px;
    margin-bottom:20px;
    font-size:14px;
  }

  .m-viewpic{
    float:right;
    margin-right:50px;
  }

  .m-placeholder{
    position:relative;
    clear:both;
  }

  #newTableTitleHint {
    width: 100%;
    text-align: center;
    margin-top: 60px;
    margin-bottom: 10px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #newTableTitleHint_2 {
    width: 100%;
    text-align: center;
    margin-top: 27px;
    margin-bottom: 10px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  .m-sonItem {
    line-height:20px;
    height:20px;
    margin-left:30px;
    margin-bottom: 10px;
  }

  .m-hp-center {
    width: 80px;
    display: inline-block;
  }

  .m-span-label {
    position: relative;
    width: 110px;
    text-align: right;
    line-height:12px;
    height:12px;
    display: inline-block;
    font-size:14px;
  }

  .m-label-addtional-for-pdf{
    font-weight:bold;
    color:#000;
  }

  .m-span-label-long {
    position: relative;
    width: 150px;
    text-align: right;
    display: inline-block;
    font-size:14px;

  }

  .m-single {
    position:relative;
    float:left;
    left:37px;
    margin-bottom:10px;
   }

  .m-single-line {
    clear:both;
    float:left;
    width:auto;
    margin-left:25px;
    text-align:right;
    margin-top:10px;
    display:inline-block;
  }

  #drillOperatetemplateList{
    position:relative;
    text-align: center;
  }


</style>

<style>

  /*.ivu-table-large td {*/
    /*color: #136BBD !important;*/
  /*}*/

  .ivu-table .m-table-row-pdf-style td{
    font-weight:bold;
    color: #000000;
  }


  .ivu-table .m-table-row-style td{
    color: #136BBD;
  }

  /***********修改table表格样式--深色系**********/
  .ivu-table-wrapper.default {
    /*border-bottom: 1px solid #000000;*/

    /*background: none!important;*/
  }

  .default .ivu-table-border td {
     border: 1px solid #000000;
   }

  .default .ivu-table-border th {
    border: 1px solid #000000;
    border-bottom: 0;
  }

</style>

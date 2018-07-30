<template>
    <div id="view_soil_drill_record">

      <Breadcrumb style="text-align: left; margin-left:100px;margin-bottom:-40px;" separator=">"
                  v-show="!ifShowImageFlag">
        <BreadcrumbItem to="/">首页</BreadcrumbItem>
        <BreadcrumbItem to="/soil_entrance">土壤类记录表</BreadcrumbItem>
        <BreadcrumbItem to="/soil_list/0">电子土壤钻孔记录表</BreadcrumbItem>
        <BreadcrumbItem>查看过往记录</BreadcrumbItem>
      </Breadcrumb>

      <div id="newTableTitleHint">
        {{record_table_name}}
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

        <div id="drillOperateRecordList" v-show="!ifShowLoadingNowFlag && table_view_data_arr.length>0">
          <Table size="large" ref="operateRecordTable" border :width="tableViewRealWidth" :style="'left:'+tableViewLeftEdge+'px;'"
                 :columns="table_view_column_arr"
                 :data="table_view_data_arr"
                 disabled-hover>
          </Table>
        </div>

        <div class="m-smallTitle" style="padding-top:30px;">【附件】：拍摄照片列表</div>
        <div class="m-picList">
          <div :id="'pic_'+(index+1)" class="m-picSingleInfoLine" v-for="(item,index) in alreadyUploadedImagesList">
          <span class="m-picfilename">{{index+1}}、图片说明：{{item.comment==''?'（无）': item.comment}}</span>
          <span
            class="m-viewpic"><Button size="small" type="success" @click="openViewOneImage(index)">点击打开图片</Button></span>
          </div>
          <div style="margin-top:-30px;padding-bottom:20px;" v-show="alreadyUploadedImagesList.length==0">（没有上传照片）</div>
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
        <div class="m-inscribe-date">填表日期：
          <span style="color:#136BBD">{{record_date}}</span>
        </div>
        <br>
        <br>
        <div id="currentFillInStatusHintContainer" style="margin-top:15px">
        <Button type="primary" size="large" @click="readyForEditAgain">点击重新编辑</Button>
        </div>
        <br>
        <br>
        <br>
        <div id="currentFillInStatusHintContainer" style="margin-top:15px">
          <Button type="primary" size="large" @click="getPdf()">输出成PDF文件</Button>
        </div>
        <br>
        <br>
        <br>
      </div>

      <div id="pdfDom" style="display:none">
        <div id="newTableTitleHint">
          {{record_table_name}}
        </div>
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

        <div id="drillOperateRecordList" v-show="!ifShowLoadingNowFlag && table_view_data_arr.length>0">
          <Table size="large" ref="operateRecordTable" border :width="tableViewRealWidth" :style="'left:'+tableViewLeftEdge+'px;'"
                 :columns="table_view_column_arr"
                 :data="table_view_data_arr"
                 disabled-hover>
          </Table>
        </div>

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
        <div class="m-inscribe-date">填表日期：
          <span style="color:#136BBD">{{record_date}}</span>
        </div>
        <br>
        <br>



      </div>
      <Card shadow :style="'background-color:#eeeeee;z-index:1001;width:'+imgShowContainerRealWidth+'px;height:'+imgShowContainerRealHeight+'px;position:fixed;top:50px;left:'+imgShowContainerEdgeW+'px;'" v-show="ifShowImageFlag">
        <div style="position:relative;">
          <span class="u-imgBasicInfo" v-show="imgSelfShowFlag">图片文件名：{{currentShowImageFileName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{currentShowImageDateTime}}</span>
          <span class="u-imgCloseBtn"><Button type="primary" @click="closeImageShow">关闭图片</Button></span>
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

      <circleLoading id="loadingEntityForViewSoilDrillRecord" v-show="ifShowLoadingNowFlag"></circleLoading>

    </div>
</template>

<script>
  export default
  {

    name: "view_soil_drill_record",

    data() {
      return {
        table_data_arr:[],
        table_column_arr:[],
        ifShowLoadingNowFlag:true,
        currentRecordId:'',
        ifShowImageFlag:false,
        openTheDatePickPanelFlag:false,
        table_view_column_arr: [],
        table_view_data_arr: [],
        tableViewLeftEdge:0,
        tableViewRealWidth:743,
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
        record_table_name:'',
        record_date:''
      }
    },
    mounted: function ()
    {

      this.initTable();

      document.body.scrollTop = 0;

      window.scrollTo(0, 0);

      this.currentRecordId = Number(this.$route.params.id);

      //console.log("this.currentRecordId=="+this.currentRecordId);

      //this.currentRecordId = 1

      //$route为当前router跳转对象里面可以获取name、path、query、params等

      //$router为VueRouter实例，想要导航到不同URL，则使用$router.push方法

      //返回上一个history也是使用$router.go方法



      this.getPointedSoilDrillRecord();

      this.rearrangeUIAfterResizeShowArea();


    },
    methods:{
      initTable() {
        this.table_column_arr = [];
        this.table_column_arr.push({type: 'selection', width: 60, align: 'center'});
        this.table_column_arr.push({
          title: '记录名称', key: 'name', width: 350, align: 'left', render: (h, params) => {
          return h('span', {
            domProps: {
              innerHTML: params.row.name,
              title: '点击查看详情'
            },
            style: {
              cursor: "pointer",
              color: "#007FFF"
            },
            on: {
              click: () => {
              // this.viewOneRecord(`${params.row._index}`);
            }
          }
        })
      }
      });

        this.table_column_arr.push({title: '创建记录的时间', key: 'create_dt', width: 200, align: 'center'});
        this.table_column_arr.push({title: '记录人', key: 'person', width: 100, align: 'center'});
        this.table_column_arr.push({title: '照片', key: 'photo', width: 80, align: 'center'});
        this.table_column_arr.push({title: '最新编辑的时间', key: 'edit_dt', width: 200, align: 'center'});

        this.table_data_arr = [];
        this.table_data_arr.push({
          name: '红桥区二号院实地勘测', create_dt: '2018-07-05 15:30', person: '朱小雨',
          photo: '有', edit_dt: '2018-07-05 18:06', id: 1001
        });
        this.table_data_arr.push({
          name: '邕江支流拐弯处108号口岸附近采样',
          create_dt: '2018-07-07 14:00',
          person: '聂佳琳',
          photo: '无',
          edit_dt: '2018-07-07 17:21',
          id: 1002
        });
        this.table_data_arr.push({
          name: '龙湖工业园C区土壤采点',
          create_dt: '2018-07-09 11:00',
          person: '张卫',
          photo: '有',
          edit_dt: '2018-07-10 2:10',
          id: 1003
        });
      },
      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      },

      initReadyOK()
      {
        this.ifShowLoadingNowFlag = false;
        this.rearrangeUIAfterResizeShowArea();
      },

      getPointedSoilDrillRecord(){

        let params = new URLSearchParams();

        params.append('record_id', this.currentRecordId);

        this.axios({
          method: 'post',
          url: 'http://datestpy.neuseer.cn/select_pointed_soil_drill_record',
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

          let tableFieldsArr = ['id', 'record_table_name', 'record_person_name', 'record_date', 'first_submit_time', 'latest_save_time', 'neishen_signature', 'dikuai_name', 'dikuai_code', 'budian_person', 'budian_date', 'caiyang_date', 'caiyang_person', 'weather_info', 'dianwei_number', 'jingdu', 'weidu', 'caiyang_site', 'drill_person_name', 'drill_person_contact', 'drill_depth', 'drill_diameter', 'drill_method', 'drill_machine_model', 'chujian_water_level', 'zhikong_depth', 'arr_sample_number', 'arr_zuanjin_depth', 'arr_diceng_describe', 'arr_wuran_describe', 'arr_caiyang_depth','arr_photo_filepath','arr_photo_comment','arr_photo_datetime'];

          //console.log("result.data.result=="+result.data.result);

          let res = JSON.parse(result.data.result);

          //console.log("res1111=="+res)

          this.record_table_name = res[0][tableFieldsArr.indexOf('record_table_name')];

          console.log("this.record_table_name=="+this.record_table_name);

          this.record_person_name = res[0][tableFieldsArr.indexOf('record_person_name')];

        console.log("this.record_person_name=="+this.record_person_name);

          this.record_date = res[0][tableFieldsArr.indexOf('record_date')];

        console.log("this.record_table_name=="+this.record_table_name);

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


          // if(res[0][tableFieldsArr.indexOf('arr_photo_filepath')].indexOf("**")>-1)
          // {
          //   this.arr_photo_filepath = res[0][tableFieldsArr.indexOf('arr_photo_filepath')].split("**");
          // }

        this.arr_photo_filepath = res[0][tableFieldsArr.indexOf('arr_photo_filepath')].split("**");

          // if(res[0][tableFieldsArr.indexOf('arr_photo_comment')].indexOf("**")>-1)
          // {
          //   this.arr_photo_comment = res[0][tableFieldsArr.indexOf('arr_photo_comment')].split("**");
          // }

        this.arr_photo_comment = res[0][tableFieldsArr.indexOf('arr_photo_comment')].split("**");

          // if(res[0][tableFieldsArr.indexOf('arr_photo_datetime')].indexOf("**")>-1)
          // {
          //   this.arr_photo_datetime = res[0][tableFieldsArr.indexOf('arr_photo_datetime')].split("**");
          // }

        this.arr_photo_datetime = res[0][tableFieldsArr.indexOf('arr_photo_datetime')].split("**");

        if(this.arr_photo_filepath.length==1 && this.arr_photo_filepath[0]==''){
          this.arr_photo_filepath = [];
          this.arr_photo_comment = [];
          this.arr_photo_datetime = [];
        }


          var i;

          this.table_view_data_arr = [];

          for(i=0;i<this.arr_sample_number.length;i++)
          {
            this.table_view_data_arr.push({sample_number:this.arr_sample_number[i],zuanjin_depth:this.arr_zuanjin_depth[i],diceng_describe:this.arr_diceng_describe[i],wuran_describe:this.arr_wuran_describe[i],caiyang_depth:this.arr_caiyang_depth[i],})
          }

          this.alreadyUploadedImagesList = [];

          for(i=0;i<this.arr_photo_filepath.length;i++)
          {
            let arrr = this.arr_photo_filepath[i].split("/");
            let imgName = arrr[arrr.length-1];
            this.alreadyUploadedImagesList.push({name:imgName,url:this.arr_photo_filepath[i],comment:this.arr_photo_comment[i],dt:this.arr_photo_datetime[i]})
          }

          this.initReadyOK();

        }).catch((error) => {

          console.log("encounter453 db access error")

          this.initStaticDataDemo();

          setTimeout(this.initReadyOK, 1000);

        });
      },

      initStaticDataDemo()
      {
          this.record_table_name = '红桥区二号院实地勘测记录';

          this.dikuai_name = '世界之窗地块A';

          this.dikuai_code = 'SZ0001';
          this.budian_person = '朱小雨';
          this.budian_date = '2018年7月1日';
          this.caiyang_date = '2018年7月5日';
          this.caiyang_person = '刘明凯';
          this.weather_info = '多云转雷阵雨';
          this.dianwei_number = '78613';
          this.jingdu = '东经35度';
          this.weidu = '北纬29度';
          this.caiyang_site = '红桥区地质家属楼二号院内';

          this.drill_person_name = '朱小雨';
          this.drill_person_contact = '13526597896';
          this.drill_depth = '10';
          this.drill_method = '机械式钻井法';

          this.drill_diameter = '150';

          this.drill_machine_model = '一级钻机A08';

          this.chujian_water_level = '36';

          this.zhikong_depth = '19';

          this.record_person_name = '朱小雨';

          this.neishen_signature = '陈总办公室';

          this.record_date = "2018年7月15日";

          this.alreadyUploadedImagesList = [];

          this.alreadyUploadedImagesList.push({name:'abcdefg.jpg',url:'/static/0.jpg',comment:'土层表面纹理',dt:'2018-07-13 11:10'})
          this.alreadyUploadedImagesList.push({name:'uuuu1.jpg',url:'/static/1.jpg',comment:'13日白天阳光照射下的土',dt:'2018-07-15 15:27'})
          this.alreadyUploadedImagesList.push({name:'uuuu2.jpg',url:'/static/2.jpg',comment:'红桥区二号院土地',dt:'2018-07-14 18:11'})
          this.alreadyUploadedImagesList.push({name:'uuuu3.jpg',url:'/static/3.jpg',comment:'下雨过后的土壤',dt:'2018-07-09 20:10'})
          this.alreadyUploadedImagesList.push({name:'uuuu4.jpg',url:'/static/4.jpg',comment:'团队合作',dt:'2018-07-08 09:10'})
          this.alreadyUploadedImagesList.push({name:'uuuu5.jpg',url:'/static/5.jpg',comment:'砖红色的土层',dt:'2018-07-13 10:10'})

          this.table_view_data_arr = [];
          this.table_view_data_arr.push({sample_number: 'Y0021', zuanjin_depth: '21m', diceng_describe: '土质疏松，发黑，颗粒密度小',
            wuran_describe:'有不好的味道，黏糊糊的，估计已经变质一段时间',caiyang_depth:'37'});
          this.table_view_data_arr.push({sample_number: 'Y0049', zuanjin_depth: '16m', diceng_describe: '土块很潮湿，浅黄色，长期被水浸泡，很软',
            wuran_describe:'未见污染，未见异样气味',caiyang_depth:'11'});
          this.table_view_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
            wuran_describe:'',caiyang_depth:''});

      },

      openViewOneImage(index){

        this.imgSelfShowFlag = false;
        let selectOneObj = this.alreadyUploadedImagesList[index];
        this.currentShowImageIndex = index;
        this.ifShowImageFlag = true;
        this.currentShowImageFileName = selectOneObj.name;

        if(selectOneObj.dt != '' && selectOneObj.dt != null){
          this.currentShowImageDateTime = '（照片拍摄时间：'+selectOneObj.dt+'）';
        }else{
          this.currentShowImageDateTime = '';
        }
        this.currentShowImageURL = selectOneObj.url;
        this.currentShowImageComment = selectOneObj.comment;
        this.imgObj = new Image();
        this.imgObj.src = this.currentShowImageURL;
        this.imgObj.onload = this.getImageLoadedHandler
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
            bh = this.imgShowContainerRealHeight - 95;
            bw = Math.floor(aw * bh / ah);
          }
          this.imgObj.width = bw;
          this.imgObj.height = bh;
          this.imageRealShowWidth = bw;
          this.imageRealShowHeight = bh;
          this.imgSelfShowFlag = true;
      },


      closeImageShow(){
        this.ifShowImageFlag = false;
        setTimeout(this.setScrollToBottom,10);

      },

      setScrollToBottom(){
        document.body.scrollTop = document.body.scrollHeight;
        window.scrollTo(0, document.body.scrollHeight);
      },

      rearrangeUIAfterResizeShowArea() {

        this.tableViewLeftEdge = (760 - this.tableViewRealWidth) /2;

        this.imgShowContainerEdgeW = (document.body.offsetWidth - this.imgShowContainerRealWidth)/2;

        this.imgShowContainerRealHeight = document.documentElement.clientHeight - 61;

        this.d("loadingEntityForViewSoilDrillRecord").style.left = (document.body.offsetWidth - this.d("loadingEntityForViewSoilDrillRecord").offsetWidth) / 2 + "px";

      },

      readyForEditAgain(){
        this.$router.push(`/edit_soil_drill_record/${this.currentRecordId}`)
      },
    }
  }
</script>

<style>

  .ivu-table-large td {
    color: #136BBD !important;
  }

</style>

<style scoped>

  #fillContentLayer {
    position: relative;
    width: 760px;
    height: auto;
    margin: auto;
  }


  #loadingEntityForViewSoilDrillRecord{
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

  #drillOperateRecordList{
    position:relative;
    text-align: center;
  }


</style>

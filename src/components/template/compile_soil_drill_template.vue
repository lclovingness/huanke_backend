<template>
    <div id="edit_soil_drill_template">

      <Breadcrumb style="text-align: left; margin-left:100px;margin-bottom:-40px;" separator=">"
                  v-show="!ifShowImageFlag">
        <BreadcrumbItem to="/">首页</BreadcrumbItem>
        <BreadcrumbItem to="/soil_entrance">土壤类记录表</BreadcrumbItem>
        <BreadcrumbItem to="/soil_list/0">电子土壤钻孔记录表</BreadcrumbItem>
        <BreadcrumbItem>{{currentFillInStatusHint}}</BreadcrumbItem>
      </Breadcrumb>

      <div id="newTableTitleHint">
        电子土壤钻孔记录表模板 之 <span style="font-family:'宋体'">“</span>{{template_table_name}}<span style="font-family:'宋体'">”</span>
      </div>


      <div id="fillInContent" v-show="!ifShowImageFlag">

        <hr style="margin-top:30px;height:1px;border:none;border-top:1px dashed gray;"/>

          <div class="m-smallTitle">1、基本信息</div>

          <div class="m-sonItem"><span class="m-span-label">地块名称：</span>

            <span><Input v-model="dikuai_name"

                         style="width: 200px"
                         size="default">
                  </Input>
            </span>
            <span class="m-hp-center">&nbsp;</span>
            <span  class="m-span-label">地块编码：</span>
            <span><Input v-model="dikuai_code"

                         style="font-size:16px;width: 200px"
                         size="default">
              </Input>
            </span>
          </div>

          <div><span class="m-span-label">布点人员：</span>

            <span><Input v-model="budian_person"

                         style="width: 200px"
                         size="default">
              </Input>
            </span>
            <span class="m-hp-center">&nbsp;</span>
            <span class="m-span-label">布点日期：</span>
            <span><DatePicker :value="budian_date" v-model="budian_date" format="yyyy年M月d日" type="date" placeholder="（请点击选择）" style="width: 200px"></DatePicker>
            </span>
          </div>

        <div class="m-smallTitle">2、点位信息</div>

        <div class="m-sonItem"><span class="m-span-label">采样日期：</span>

          <span><DatePicker :value="caiyang_date" v-model="caiyang_date" format="yyyy年M月d日" type="date" placeholder="（请点击选择）" style="width: 200px"></DatePicker></span>
          <span class="m-hp-center">&nbsp;</span>
          <span  class="m-span-label">采样人员：</span>
          <span><Input v-model="caiyang_person"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">天气：</span>
          <span>
            <Select v-model="weather_info" size="large" style="width:85px;">
              <Option value="晴天" key="sunshine">晴 天</Option>
              <Option value="雨天" key="rainy">雨 天</Option>
              <Option value="阴天" key="cloudy">阴 天</Option>
            </Select>
          </span>
          <span class="m-hp-center-specifal">&nbsp;</span>
          <span class="m-span-label">点位编号：</span>
          <span><Input v-model="dianwei_number"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">经度：</span>

          <span><Input v-model="jingdu"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
          <span class="m-hp-center">&nbsp;</span>
          <span class="m-span-label">纬度：</span>
          <span><Input v-model="weidu"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-single"><span class="m-span-label">采样地点：</span>

          <span><Input v-model="caiyang_site"

                       style="width: 400px"
                       size="default">
            </Input>
            </span>

        </div>

        <div class="m-smallTitle">3、钻孔信息</div>

        <div class="m-sonItem"><span class="m-span-label">钻孔负责人：</span>

          <span><Input v-model="drill_person_name"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
          <span class="m-hp-center">&nbsp;</span>
          <span  class="m-span-label">联系方式：</span>
          <span><Input v-model="drill_person_contact"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">钻孔深度(m)：</span>

          <span><Input v-model="drill_depth"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
          <span class="m-hp-center">&nbsp;</span>
          <span  class="m-span-label">钻孔直径(mm)：</span>
          <span><Input v-model="drill_diameter"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">钻孔方法：</span>

          <span><Input v-model="drill_method"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
          <span class="m-hp-center">&nbsp;</span>
          <span  class="m-span-label">钻机型号：</span>
          <span><Input v-model="drill_machine_model"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-sonItem"><span class="m-span-label">初见水位(m)：</span>

          <span><Input v-model="chujian_water_level"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
          <span class="m-hp-center">&nbsp;</span>
          <span  class="m-span-label">止孔深度(m)：</span>
          <span><Input v-model="zhikong_depth"

                       style="width: 200px"
                       size="default">
            </Input>
            </span>
        </div>

        <div class="m-smallTitle">4、钻进操作记录</div>

        <div id="drillOperateRecordList">
          <Table size="large" ref="operateRecordTable" border :width="tableRealWidth" :style="'left:'+tableLeftEdge+'px;'"
                 :columns="table_column_arr"
                 :data="table_data_arr"></Table>
        </div>

        <div class="m-placeholder">&nbsp;&nbsp;</div>

        <hr style="position:relative;margin-top:20px;margin-bottom:20px;height:2px;border:none;border-top:1px dashed gray;"/>

          <div class="m-single-line"><span class="m-span-label-long">钻孔负责人：</span>

            <span><Input ref="drill_twin_input" v-model="drill_person_name"

                         style="width: 100px;display:inline-block;"
                         size="default">
              </Input>
              </span>

          </div>
          <br>
          <div class="m-single-line"><span class="m-span-label-long">记录人：</span>

            <span><Input v-model="record_person_name"
                         style="width: 100px;display:inline-block;"
                         size="default">
              </Input>
              </span>

          </div>
          <br>
          <div class="m-single-line"><span class="m-span-label-long">采样单位的内审签名：</span>

            <span><Input v-model="neishen_signature" style="width: 200px;display:inline-block;" size="default">
              </Input>
              </span>

          </div>
        <br>
        <br>
        <br>
        <br>
        <br>

        <br>
        <br>
        <br>
        <div><Button type="primary" size="large" @click="saveFillInHandler">保存模板</Button></div>
        <br>
        <br>
      </div>


    </div>
</template>

<script>
  export default
  {
    name: "compile_soil_drill_template",

    data() {
      return{
        defaultList: [
          {
            'name': 'a42bdcc1178e62b4694c830f028db5c0',
            'url': 'https://o5wwk8baw.qnssl.com/a42bdcc1178e62b4694c830f028db5c0/avatar'
          },
          {
            'name': 'bc7521e033abdd1e92222d733590f104',
            'url': 'https://o5wwk8baw.qnssl.com/bc7521e033abdd1e92222d733590f104/avatar'
          }
        ],
        template_table_name:'',
        update_date_time:'',
        uploadList:[],
        ifShowLoadingNowFlag:true,
        iftemplateNameEditFlag:false,
        ifShowImageFlag:false,
        currentFillInStatusHint:'',
        openTheDatePickPanelFlag:false,
        table_column_arr: [],
        table_data_arr: [],
        tableLeftEdge:0,
        tableRealWidth:743,
        template_date:'',
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
        addtionLeftEdge:'',
        addtionRightEdge:'',
        addtionRightEdge:'',
        currentTemplateId:'',
        first_submit_time:'',
        latest_save_time:'',
        hintDelImgIFInEditAlreadyRecordStatus:'',
        alreadyUploadedFileAmount:0,
        curBatchUploadListAmount:0,
        curNowUploadedOKCount:0,
        templateList:[],
        selectedTemplateValue:''
      }
    },
    mounted: function ()
    {

      window.scrollTo(0, 0);

      this.template_table_name = this.$store.state.currentTemplateName;

      this.currentTemplateId = Number(this.$route.params.id);

      this.table_column_arr = [];
      this.table_column_arr[0]={title:'样品编号',key:'sample_number',width:100,align: 'left',render:(h,params)=>{

        return h('div',[
          h('Input', {
            props: {
              value: this.arr_sample_number[params.row._index]
            },
            on: {
              'on-change': (e) => {
                this.arr_sample_number[params.row._index] = e.target.value;
              }
            }
          })
        ])
      }};
      this.table_column_arr[1]={title:'钻进深度',key:'zuanjin_depth',border:false,width:100,align: 'center',children: [
          {
            title: '（m）',
            key: 'zuanjin_depth',
            align: 'center',
            width: 100,
            render:(h,params)=>{
                return h('div',[
                  h('Input', {
                    props: {
                      value: this.arr_zuanjin_depth[params.row._index]
                    },
                    on: {
                      'on-change': (e) => {
                        this.arr_zuanjin_depth[params.row._index] = e.target.value;
                      }
                    }
                  })
                ])
            }}]
      };
      this.table_column_arr[2]={title:'地层描述',key:'diceng_describe',width:220,children: [
          {
            title: '土质分类、密度、颜色、湿度',
            key: 'diceng_describe',
            align: 'center',
            width: 220,
            render:(h,params)=>{
              return h('div',[
                h('Input', {
                  props: {
                    autosize:true,
                    type: 'textarea',
                    value: this.arr_diceng_describe[params.row._index]
                  },
                  on: {
                    'on-change': (e) => {
                        this.arr_diceng_describe[params.row._index] = e.target.value;
                     }
                  }
                })
              ])}
          }],align: 'center'};

      this.table_column_arr[3]={title:'污染描述',key:'wuran_describe',width:220,children: [
          {
            title: '气味、污染痕迹、油状物等',
            key: 'wuran_describe',
            align: 'center',
            width: 220,
            render:(h,params)=>{
            return h('div',[
              h('Input', {
                props: {
                  autosize:true,
                  type: 'textarea',
                  value: this.arr_wuran_describe[params.row._index]
                },
                on: {
                  'on-change': (e) => {
                  this.arr_wuran_describe[params.row._index] = e.target.value;
                    }
                }
              })
            ])}
    }],align: 'center'};

      this.table_column_arr[4]={title:'采样深度',key:'caiyang_depth',width:100,align: 'center',children: [
      {
        title: '（m）',
        key: 'caiyang_depth',
        align: 'center',
        width: 100,
        render:(h,params)=>{

        return h('div',[
          h('Input', {
            props: {
              value: this.arr_caiyang_depth[params.row._index]
            },
            on: {
              'on-change': (e) => {
                this.arr_caiyang_depth[params.row._index] = e.target.value;
              }
            }
          })
        ])
      }}]
    };

      this.table_data_arr = [];
      this.table_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
        wuran_describe:'',caiyang_depth:''});

      if(this.currentTemplateId == 0)
      {

        this.currentFillInStatusHint = '新建模板';

        this.initReadyOK();

      } else {

        this.currentFillInStatusHint = '编辑已有模板';

        this.getPointedSoilDrillRecord();
      }

      this.rearrangeUIAfterResizeShowArea();
    },
    methods:{

      onReadyForUploadFileStarter(){
        this.curNowUploadedOKCount = 0;
        this.alreadyUploadedFileAmount = this.uploadList.length;
      },

      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      }
      ,

      readyForCreateNewTemplate(){

      },

      handleBeforeUpload(){
        //得出本次上传文件的数量
        this.curBatchUploadListAmount = this.uploadList.length + 1 - this.alreadyUploadedFileAmount;
        if(!this.uploadFileNowFlag)
        {
          this.uploadFileNowFlag = true;
          this.$Spin.show({
            render: (h) => {
            return h('div', [
              h('Icon', {
                'class': 'demo-spin-icon-load',
                props: {
                  type: 'ios-loading',
                  size: 20
                }
              }),
              h('div', '正在上传图片文件，请稍候...')
            ])
          }
        });
        }
      },

      handleUploadFileSuccess(res,file)
      {
        // console.log("v="+JSON.stringify(res));
        // console.log("file="+JSON.stringify(file));
        // //this.$refs.uploadEntity.clearFiles();
        setTimeout(this.delayShowUploadOK,200,file);

      },

      delayShowUploadOK(file){
        this.alreadyUploadedImagesList.push({name:file.name,url:'http://huankepy.neuseer.cn/static/huanke/'+file.name,comment:file.name,dt:''});

        this.curNowUploadedOKCount+=1;
        if(this.curNowUploadedOKCount == this.curBatchUploadListAmount)
        {
          this.uploadFileNowFlag = false;
          this.$Spin.hide();
          setTimeout(() => {alert("所选择的图片文件全部上传成功！")}, 500);
        }
      },

      initReadyOK()
      {
        this.ifShowLoadingNowFlag = false;
      },

      deleteOnePicHandler(index)
      {
        this.currentShowImageFileName = this.alreadyUploadedImagesList[index].name;
        this.currentShowImageIndex = index;
        this.ifDeleteOneImageHintFlag=true;
        if(this.currentTemplateId != 0){
          this.hintDelImgIFInEditAlreadyRecordStatus = '（提示：在记录表的底部点击保存填写内容后生效）';
        }
      },

      getPointedSoilDrillRecord(){

        let params = new URLSearchParams();

        params.append('template_id', this.currentTemplateId);

        this.axios({
          method: 'post',
          url: 'http://huankepy.neuseer.cn/select_pointed_soil_drill_template',
          data: params
        }).then((result) => {

        let tableFieldsArr = this.$store.state.soil_drill_template_table_fields;

        let res = JSON.parse(result.data.result);

        this.template_table_name = res[0][tableFieldsArr.indexOf('template_table_name')];
        this.update_date_time = res[0][tableFieldsArr.indexOf('update_date_time')];
        this.record_person_name = res[0][tableFieldsArr.indexOf('record_person_name')];
        this.neishen_signature = res[0][tableFieldsArr.indexOf('neishen_signature')];
        this.dikuai_name = res[0][tableFieldsArr.indexOf('dikuai_name')];
        this.dikuai_code = res[0][tableFieldsArr.indexOf('dikuai_code')];
        this.budian_person = res[0][tableFieldsArr.indexOf('budian_person')];
        this.budian_date = res[0][tableFieldsArr.indexOf('budian_date')];
        this.caiyang_date = res[0][tableFieldsArr.indexOf('caiyang_date')];
        this.caiyang_person = res[0][tableFieldsArr.indexOf('caiyang_person')];
        this.weather_info = res[0][tableFieldsArr.indexOf('weather_info')];
        this.dianwei_number = res[0][tableFieldsArr.indexOf('dianwei_number')];
        this.jingdu = res[0][tableFieldsArr.indexOf('jingdu')];
        this.weidu = res[0][tableFieldsArr.indexOf('weidu')];
        this.caiyang_site = res[0][tableFieldsArr.indexOf('caiyang_site')];
        this.drill_person_name = res[0][tableFieldsArr.indexOf('drill_person_name')];
        this.drill_person_contact = res[0][tableFieldsArr.indexOf('drill_person_contact')];
        this.drill_depth = res[0][tableFieldsArr.indexOf('drill_depth')];
        this.drill_diameter = res[0][tableFieldsArr.indexOf('drill_diameter')];
        this.drill_method = res[0][tableFieldsArr.indexOf('drill_method')];
        this.drill_machine_model = res[0][tableFieldsArr.indexOf('drill_machine_model')];
        this.chujian_water_level = res[0][tableFieldsArr.indexOf('chujian_water_level')];
        this.zhikong_depth = res[0][tableFieldsArr.indexOf('zhikong_depth')];


        this.arr_sample_number = res[0][tableFieldsArr.indexOf('arr_sample_number')].split("**");
        this.arr_zuanjin_depth = res[0][tableFieldsArr.indexOf('arr_zuanjin_depth')].split("**");
        this.arr_diceng_describe = res[0][tableFieldsArr.indexOf('arr_diceng_describe')].split("**");
        this.arr_wuran_describe = res[0][tableFieldsArr.indexOf('arr_wuran_describe')].split("**");
        this.arr_caiyang_depth = res[0][tableFieldsArr.indexOf('arr_caiyang_depth')].split("**");

        this.table_data_arr = [];

        for (var i = 0; i < this.arr_sample_number.length; i++) {
          this.table_data_arr.push({
            sample_number: this.arr_sample_number[i],
            zuanjin_depth: this.arr_zuanjin_depth[i],
            diceng_describe: this.arr_diceng_describe[i],
            wuran_describe: this.arr_wuran_describe[i],
            caiyang_depth: this.arr_caiyang_depth[i]
          })
        }

        this.initReadyOK();

      }).catch((error) => {

          console.log("encounter db access error")

        this.initReadyOK();

      });
      },



      saveFillInHandler(){
        //调用 py 程序保存到数据库表中
        this.insertOrUpdateSoilDrillTable();
      },

      handleChange(dv){
        this.template_date = dv;
      },
      handleClear(){
        this.openTheDatePickPanelFlag = false;
      },
      handleOk(){
        this.openTheDatePickPanelFlag = false;
      },
      handleClick(){
        this.openTheDatePickPanelFlag = !this.openTheDatePickPanelFlag;
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

        this.tableLeftEdge = (760 - this.tableRealWidth) /2;

        this.imgShowContainerEdgeW = (document.body.offsetWidth - this.imgShowContainerRealWidth)/2;

        this.addtionLeftEdge = (document.body.offsetWidth - 760)/2;

        this.addtionRightEdge = (document.body.offsetWidth - 760)/2

        this.imgShowContainerRealHeight = document.documentElement.clientHeight - 60;

      },

      insertOrUpdateSoilDrillTable(){
        let params = new URLSearchParams();

        let operateTableActionStr;

        if(this.currentTemplateId != 0){
          params.append('template_id', this.currentTemplateId);
          operateTableActionStr = '/update_soil_drill_template';
        } else {
          operateTableActionStr = '/insert_soil_drill_template';
        }

        this.update_date_time = new Date().Format("yyyy-MM-dd hh:mm");

        let budianDate;

        if(this.budian_date == ""){
          budianDate = '';
        }else{
          budianDate = new Date(this.budian_date).Format("yyyy-MM-dd")
        }

        let caiyangDate;

        if(this.caiyang_date == ""){
          caiyangDate = '';
        }else{
          caiyangDate = new Date(this.caiyang_date).Format("yyyy-MM-dd")
        }

        params.append('template_table_name', this.template_table_name);
        params.append('update_date_time', this.update_date_time);
        params.append('record_person_name', this.record_person_name);
        params.append('neishen_signature', this.neishen_signature);
        params.append('dikuai_name', this.dikuai_name);
        params.append('dikuai_code', this.dikuai_code);
        params.append('budian_person', this.budian_person);
        params.append('budian_date', budianDate);
        params.append('caiyang_date', caiyangDate);
        params.append('caiyang_person', this.caiyang_person);
        params.append('weather_info', this.weather_info);
        params.append('dianwei_number', this.dianwei_number);
        params.append('jingdu', this.jingdu);
        params.append('weidu', this.weidu);
        params.append('caiyang_site', this.caiyang_site);
        params.append('drill_person_name', this.drill_person_name);
        params.append('drill_person_contact', this.drill_person_contact);
        params.append('drill_depth', this.drill_depth);
        params.append('drill_diameter', this.drill_diameter);
        params.append('drill_method', this.drill_method);
        params.append('drill_machine_model', this.drill_machine_model);
        params.append('chujian_water_level', this.chujian_water_level);
        params.append('zhikong_depth', this.zhikong_depth);
        params.append('arr_sample_number', this.arr_sample_number.join("**"));
        params.append('arr_zuanjin_depth', this.arr_zuanjin_depth.join("**"));
        params.append('arr_diceng_describe', this.arr_diceng_describe.join("**"));
        params.append('arr_wuran_describe', this.arr_wuran_describe.join("**"));
        params.append('arr_caiyang_depth', this.arr_caiyang_depth.join("**"));
        params.append('arr_diceng_describe', this.arr_diceng_describe.join("**"));
        params.append('arr_wuran_describe', this.arr_wuran_describe.join("**"));
        params.append('arr_caiyang_depth', this.arr_caiyang_depth.join("**"));

        this.axios({

          method: 'post',
          url: 'http://huankepy.neuseer.cn' + operateTableActionStr,
          data: params

        }).then((res) => {


          if(res.data.result > 0)
          {
            //新建模板成功

            this.currentTemplateId = res.data.result;

          }

          alert('保存成功，点击确定查看');

          this.$router.push(`/template/view_soil_drill_template/${this.currentTemplateId}`);

        }).catch((error) => {
          alert("写入数据表失败");
          console.log("insert data to mysql error: " + error)
        });

      },

    }
  }
</script>

<style>

  .ivu-input {
    font-size: 16px !important;
  }

</style>

<style scoped>

  #fillInContent {
    clear:both;
    position: relative;
    width: 760px;
    height: auto;
    margin: auto;
  }

  #currentFillInStatusHintContainer{
    position:relative;
    float:right;
    font-size:16px;
  }

  #template_table_nameContainer{
    position:relative;
    float:left;
    width:auto;
    margin-bottom:15px;
    font-size:16px;
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

  .m-inscribe-date{
    position:relative;
    float:right;
    margin-right:30px;
    font-size:14px;
  }

  .m-smallTitle {
    text-align: left;
    padding: 20px;
    padding-top: 40px;
    font-size: 16px;
    font-weight: bold;
  }

  .m-uploadfiles-btn{
    width:auto;
    text-align: left;
    padding-left: 20px;
  }

  .m-picList{
    position:relative;
    margin-top:20px;
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
    margin-top:20px;
  }

  .m-pic-comment{
    float:left;
    display:inline-block;
    margin-left:30px;
  }

  #newTableTitleHint {
    width: 100%;
    text-align: center;
    margin-top: 70px;
    margin-bottom: 30px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  .m-sonItem {
    margin-bottom: 22px;
  }

  .m-hp-center {
    width: 80px;
    display: inline-block;
  }

  .m-hp-center-specifal {
    width: 197px;
    display: inline-block;
  }

  .m-span-label {
    position: relative;
    width: 110px;
    text-align: right;
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
    width:700px;
    margin-left:-70px;
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

  .demo-spin-icon-load{
    animation: ani-demo-spin 1s linear infinite;
  }

  #templateRegion{
    position:absolute;
    float:right;
    top:60px;
    right:60px;
  }

</style>

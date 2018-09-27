<template>
    <div id="edit_soil_drill_record">

      <Breadcrumb style="text-align: left; margin-left:50px;margin-bottom:-20px;" separator=">"
                  v-show="!ifShowImageFlag">
        <BreadcrumbItem to="/">首页</BreadcrumbItem>
        <BreadcrumbItem to="/soil_entrance">土壤类记录表</BreadcrumbItem>
        <BreadcrumbItem to="/soil_list/0">电子土壤钻孔记录表</BreadcrumbItem>
        <BreadcrumbItem>填写记录</BreadcrumbItem>
      </Breadcrumb>

      <div id="templateRegion" v-show="!ifShowImageFlag">
        <span><Button type="success" @click="readyForCreateNewTemplate()">新建模板
        </Button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;</span>
        <span style="border: 1px dashed #777777;padding:10px;">
        <span>选择模板：
          <Select v-model="selectedTemplateValue" style="width:auto" size="small" @on-change="echoTemplateSelectHandler()">
             <Option v-for="item in templateList" :value="item.value" :key="item.value">{{ item.label }}</Option>
          </Select>
        </span>
        <span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Button size="small" type="success"
                                                    @click="readyForApplySelectedTemplate()">应用此模板
        </Button>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          &nbsp;</span><Button size="small" type="success" :disabled="forbiddenViewTheSelectedTemplateFlag"
                               @click="readyForViewAlreadyHaveTemplate()">查看此模板
      </Button></span></span>
      </span>
      </div>

      <div id="newTableTitleHint">
        填写电子土壤钻孔记录表
      </div>

      <div id="record_table_nameContainer" :style="'left:'+addtionLeftEdge+'px'">
        ◆ 记录表名称：
        <span style="color:#b00a1a" v-if="!ifRecordNameEditFlag">{{record_table_name}}</span>
        <span style="color:#b00a1a;display:inline-block" v-else="ifRecordNameEditFlag"><Input v-model="record_table_name" style="width:250px" size="small"></Input></span>
        <span @click="ifRecordNameEditFlag=!ifRecordNameEditFlag" style="cursor:pointer">&nbsp;&nbsp;<Icon :title="ifRecordNameEditFlag?'点击锁定确认更改':'点击更名'" :type="ifRecordNameEditFlag?'locked':'edit'"></Icon></span>
      </div>

      <div id="currentFillInStatusHintContainer" :style="'right:'+addtionRightEdge+'px'">
        ◆ 当前状态：<span style="color:#b00a1a">{{currentFillInStatusHint}}</span>
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
        <!--:default-file-list="defaultList"-->
        <div class="m-smallTitle">【附件】：拍摄照片列表</div>
        <div class="m-uploadfiles-btn" @click="onReadyForUploadFileStarter">
          <Upload
            size="large"
            ref="uploadEntity"
            style="font-size:14px;"
            multiple
            :show-upload-list="false"

            :before-upload="handleBeforeUpload"
            :on-success="handleUploadFileSuccess"
            action="http://huankepy.neuseer.cn/upload">
            <Button type="default" size="large" icon="ios-cloud-upload-outline">点击上传图片</Button> &nbsp;&nbsp;（注意：可同时选择多个文件。为了保证传输稳定，建议每次上传最多不超过 8 个文件。）</Upload>
        </div>

        <div class="m-picList">
          <div :id="'pic_'+(index+1)" class="m-picSingleInfoLine" v-for="(item,index) in alreadyUploadedImagesList">
          <span class="m-picfilename"><Icon type="ios-close-circle-outline" size="24" color="#0000ff" style="cursor:pointer;vertical-align: middle" title="点击删除图片" @click="deleteOnePicHandler(index)"></Icon>&nbsp;&nbsp;{{index+1}}、添加图片说明：<Input v-model="item.comment" size="small" style="width: 290px;display:inline-block"></Input></span>
          <span class="m-viewpic"><Button size="small" type="success" @click="openViewOneImage(index)">点击预览图片</Button></span>
          </div>
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
        <div class="m-inscribe-date">填表日期：
          <span>
            <DatePicker
            :open="openTheDatePickPanelFlag"
            :value="record_date"
            confirm
            type="date"
            @on-change="handleChange"
            @on-clear="handleClear"
            @on-ok="handleOk">
            <a href="javascript:void(0)" @click="handleClick">
                <Icon type="calendar" v-show="record_date === ''"></Icon>
                <template v-if="record_date === ''">点击选择</template>
                <template style="color:#000" v-else>{{ record_date }}</template>
            </a>
            </DatePicker>
          </span>
        </div>
        <br>
        <br>
        <br>
        <div><Button type="primary" size="large" @click="saveFillInHandler">保存填写内容</Button></div>
        <br>
        <br>
      </div>

      <Card shadow :style="'background-color:#eeeeee;z-index:100;width:'+imgShowContainerRealWidth+'px;height:'+imgShowContainerRealHeight+'px;position:fixed;top:50px;left:'+imgShowContainerEdgeW+'px;'" v-show="ifShowImageFlag">
        <div style="position:relative;">
          <span class="u-imgBasicInfo" v-show="imgSelfShowFlag">图片文件名：{{currentShowImageFileName}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{currentShowImageDateTime}}&nbsp;&nbsp;&nbsp;&nbsp;<Icon type="ios-close-circle-outline" size="24" color="#0000ff" style="cursor:pointer;vertical-align: middle" title="点击删除图片" @click="deleteOnePicHandler(currentShowImageIndex)"></Icon></span>
          <span class="u-imgCloseBtn"><Button type="primary" @click="closeImageShow">关闭图片显示</Button></span>
          <!--<Icon size="26" type="close-circled" title="点击关闭图片" @click="closeImageShow"></Icon>-->
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

      <Modal
        v-model="ifDeleteOneImageHintFlag"
        title="温馨提示"
        width="500"
        @on-ok="del_one_image"
        @on-cancel="not_del_one_image">
        <p style="font-size:16px">确定要删除图片文件 <span style="color:#2D8CF0">{{currentShowImageFileName}}</span> 吗？</p>
        <p style="margin-top:20px;font-size:14px">{{hintDelImgIFInEditAlreadyRecordStatus}}</p>
      </Modal>

      <circleLoading id="loadingEntityForEditSoilDrillRecord" v-show="ifShowLoadingNowFlag"></circleLoading>

      <div v-for="item in uploadList">
        <template v-if="item.status === 'finished'">
          <img :src="item.url">

        </template>

      </div>

      <Modal
        v-model="ifCreateOneNewTemplateFlag"
        title="新建一个模板"
        width="360"
        class="vertical-center-modal"
        @on-ok="createTemplate"
        @on-cancel="cancelCreateTemplateQuit">
        <div class="m-input-template-name-box">
          <div><input type="text" placeholder="请输入模板名字..." id="newTemplateNameTB" class="input-newTemplateNameTB"
                      onfocus="this.placeholder='';"
                      onblur="this.value==''?this.placeholder='请输入模板名字...':this.placeholder='';"></div>
        </div>
      </Modal>

      <Modal
        v-model="hintTheConsequenceWhenApplyTemplateFlag"
        width="530"
        title='温馨提示'
        closable
        class="vertical-center-modal"
        @on-ok="ok_applyTemplate"
        @on-cancel="cancel_applyTemplate">
        <p class="m-modelHintWords">在应用模板后，当前您已经录入的内容将被清空，您不得不重新录入。<br><br>确定要应用此模板吗？</p>
      </Modal>

    </div>
</template>

<script>
  export default
  {
    name: "edit_soil_drill_record",

    data() {
      return{
        ifCreateOneNewTemplateFlag:false,
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
        uploadList:[],
        forbiddenViewTheSelectedTemplateFlag:true,
        ifShowLoadingNowFlag:true,
        ifRecordNameEditFlag:false,
        ifShowImageFlag:false,
        currentFillInStatusHint:'',
        openTheDatePickPanelFlag:false,
        table_column_arr: [],
        table_data_arr: [],
        tableLeftEdge:0,
        tableRealWidth:743,
        record_date:'',
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
        arr_photo_width_height:[],
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
        addtionLeftEdge:'',
        addtionRightEdge:'',
        addtionRightEdge:'',
        currentRecordId:'',
        first_submit_time:'',
        latest_save_time:'',
        hintDelImgIFInEditAlreadyRecordStatus:'',
        alreadyUploadedFileAmount:0,
        curBatchUploadListAmount:0,
        curNowUploadedOKCount:0,
        templateList:[],
        selectedTemplateValue:'(empty)',
        hintTheConsequenceWhenApplyTemplateFlag:false
      }
    },
    mounted: function ()
    {
      document.body.scrollTop = 0;

      window.scrollTo(0, 0);

      this.initPreTemplateList();
      //
      //
      //
      // this.templateList[0]={};
      // this.templateList[0].label = "（空白模板）";
      // this.templateList[0].value = "(empty)";
      // this.templateList[1]={};
      // this.templateList[1].label = "专用土壤模板一";
      // this.templateList[1].value = "template_1";

      this.uploadList = this.$refs.uploadEntity.fileList;

      this.alreadyUploadedFileAmount = this.uploadList.length;

      this.currentRecordId = Number(this.$route.params.id);

      this.alreadyUploadedImagesList = [];

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
      this.table_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
        wuran_describe:'',caiyang_depth:''});
      this.table_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
        wuran_describe:'',caiyang_depth:''});

      if(this.currentRecordId == 0){
        this.currentFillInStatusHint = '新建记录';
        this.record_table_name = this.$store.state.recordName;

        this.initReadyOK();

      } else {
        this.currentFillInStatusHint = '编辑已有记录';

        this.getPointedSoilDrillRecord();
      }

      this.rearrangeUIAfterResizeShowArea();
    },

    methods:{

      initPreTemplateList()
      {
          let params = new URLSearchParams();

          params.append('username', '');

          this.templateList=[];

          this.templateList[0]={};
          this.templateList[0].label = "（空白模板）";
          this.templateList[0].value = "(empty)";

          this.axios({

            method: 'post',
            url: 'http://huankepy.neuseer.cn/select_soil_drill_template',
            data: params

          }).then((res) => {

            if(res.data.result == '[]')
            {

              //
            }else
            {

              let receiveData = JSON.parse(res.data.result);

              let rlen = receiveData.length;

              let tableFieldsArr = this.$store.state.soil_drill_template_table_fields;

              for (var i = 0; i < rlen; i++) {

                this.templateList.push({
                  label: receiveData[i][tableFieldsArr.indexOf('template_table_name')],
                  value: receiveData[i][tableFieldsArr.indexOf('id')],
                });

              }

            }

          }).catch((error) => {

            console.log("access py error: " + error);

            this.initReadyOK();

          });
      },

      readyForApplySelectedTemplate()
      {
        //打算应用选择的模板
        this.hintTheConsequenceWhenApplyTemplateFlag = true;
      },

      ok_applyTemplate(){
        let params = new URLSearchParams();

        params.append('template_id', this.selectedTemplateValue);

        this.axios({
          method: 'post',
          url: 'http://huankepy.neuseer.cn/select_pointed_soil_drill_template',
          data: params
        }).then((result) => {

          let tableFieldsArr = this.$store.state.soil_drill_template_table_fields;

          let res = JSON.parse(result.data.result);

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

          this.drill_depth = res[0][tableFieldsArr.indexOf('drill_depth')]

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

          for(var i=0;i<1;i++)
          {
            this.table_data_arr.push({sample_number:this.arr_sample_number[i],zuanjin_depth:this.arr_zuanjin_depth[i],diceng_describe:this.arr_diceng_describe[i],wuran_describe:this.arr_wuran_describe[i],caiyang_depth:this.arr_caiyang_depth[i],})
          }

        this.table_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
          wuran_describe:'',caiyang_depth:''});
        this.table_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
          wuran_describe:'',caiyang_depth:''});


        });

      },

      cancel_applyTemplate(){

      },

      readyForViewAlreadyHaveTemplate(){
        // //预览已有的模板
        // this.$router.push(`/template/view_soil_drill_template/${this.selectedTemplateValue}`);
        let routeData = this.$router.resolve({
          name: "ViewSoilDrillTemplate", // 注意这里的 name 要和路由中设定的一样
          params:{id:this.selectedTemplateValue},
        });
        window.open(routeData.href, '_blank');
      },

      echoTemplateSelectHandler(){
        if(this.selectedTemplateValue == "(empty)"){
          this.forbiddenViewTheSelectedTemplateFlag = true;
        } else {
          this.forbiddenViewTheSelectedTemplateFlag = false;
        }
      },

      createTemplate() {

        let str = this.d("newTemplateNameTB").value.trim();

        if (str == "") {

          this.$Message.info('请输入有效的模板名称');

          setTimeout(this.atOnceReShow, 0);

        } else if (this.repeatNameJudgement(str)) {

          this.$Message.info('该模板名称已存在，请重新命名');

          //this.waitReadyForCreateNewFla = false;

          setTimeout(this.atOnceReShow, 0);

        } else if (escape(str).indexOf("%u") != -1 && str.length > 20) {

          alert("模板命名请不要超过20个汉字的长度");

          setTimeout(this.atOnceReShow, 0);

        } else if (str.length > 30) {

          alert("模板命名请不要超过30个英文半角字符的长度");

          setTimeout(this.atOnceReShow, 0);

        } else {

          this.$store.state.currentTemplateName = str;

          this.$store.state.currentSelectedTemplateID = 0;

          this.$router.push('/template/compile_soil_drill_template/0');

        }

      }
      ,

      repeatNameJudgement(nameStr) {

        let len = this.templateList.length;
        let repeatFlag = false;
        for (var i = 0; i < len; i++) {
          if (this.templateList[i].label == nameStr) {
            repeatFlag = true;
            break;
          }
        }
        return repeatFlag;
      },

      atOnceReShow(){
        this.ifCreateOneNewTemplateFlag = true;
      },

      cancelCreateTemplateQuit() {
        //this.$Message.info('Clicked cancel');
      }
      ,

      onReadyForUploadFileStarter(){
        this.curNowUploadedOKCount = 0;
        this.alreadyUploadedFileAmount = this.uploadList.length;
      },

      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      }
      ,

      readyForCreateNewTemplate()
      {
        this.ifCreateOneNewTemplateFlag = true;
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
        console.log("file="+JSON.stringify(file));
        // //this.$refs.uploadEntity.clearFiles();
        setTimeout(this.delayShowUploadOK,200,file);

      },

      getUploadImageWidthAndHeight(lockIndex,url){
        let imgObj;
        let ownerHost = this;
        var getImageLoadedHandler = function () {
          //console.log(imgObj.width + "=" + imgObj.height);
          ownerHost.alreadyUploadedImagesList[lockIndex]["width"]=imgObj.width;
          ownerHost.alreadyUploadedImagesList[lockIndex]["height"]=imgObj.height;
          //console.log(JSON.stringify(ownerHost.alreadyUploadedImagesList))
        }

        imgObj = new Image();
        imgObj.src = url;
        imgObj.onload = getImageLoadedHandler;
      },

      delayShowUploadOK(file){
        // 暂时取不到上传的照片的拍摄时间，因此，就先用上传照片完成的时间来替代吧。
        let dt = new Date().Format("yyyy-MM-dd hh:mm");
        this.alreadyUploadedImagesList.push({name:file.name,url:'http://huankepy.neuseer.cn/static/huanke/'+file.name,comment:file.name.split(".")[0],dt:dt});
        this.getUploadImageWidthAndHeight(this.alreadyUploadedImagesList.length-1,'http://huankepy.neuseer.cn/static/huanke/'+file.name);
        this.curNowUploadedOKCount+=1;
        if(this.curNowUploadedOKCount == this.curBatchUploadListAmount)
        {
          this.uploadFileNowFlag = false;
          this.$Spin.hide();
          setTimeout(() => {console.log(JSON.stringify(this.alreadyUploadedImagesList));alert("所选择的图片文件全部上传成功！")}, 500);
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
        if(this.currentRecordId != 0){
          this.hintDelImgIFInEditAlreadyRecordStatus = '（提示：在记录表的底部点击保存填写内容后生效）';
        }
      },

      getPointedSoilDrillRecord(){

        let params = new URLSearchParams();

        params.append('record_id', this.currentRecordId);

        this.axios({
          method: 'post',
          url: 'http://huankepy.neuseer.cn/select_pointed_soil_drill_record',
          data: params
        }).then((result) => {

        let tableFieldsArr = ['id', 'record_table_name', 'record_person_name', 'record_date', 'first_submit_time', 'latest_save_time', 'neishen_signature', 'dikuai_name', 'dikuai_code', 'budian_person', 'budian_date', 'caiyang_date', 'caiyang_person', 'weather_info', 'dianwei_number', 'jingdu', 'weidu', 'caiyang_site', 'drill_person_name', 'drill_person_contact', 'drill_depth', 'drill_diameter', 'drill_method', 'drill_machine_model', 'chujian_water_level', 'zhikong_depth', 'arr_sample_number', 'arr_zuanjin_depth', 'arr_diceng_describe', 'arr_wuran_describe', 'arr_caiyang_depth','arr_photo_filepath','arr_photo_comment','arr_photo_datetime'];

        let res = JSON.parse(result.data.result);

        this.record_table_name = res[0][tableFieldsArr.indexOf('record_table_name')];
        this.record_person_name = res[0][tableFieldsArr.indexOf('record_person_name')];
        this.record_date = res[0][tableFieldsArr.indexOf('record_date')];
        this.first_submit_time = res[0][tableFieldsArr.indexOf('first_submit_time')];
        this.latest_save_time = res[0][tableFieldsArr.indexOf('latest_save_time')];
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

        this.arr_photo_filepath = res[0][tableFieldsArr.indexOf('arr_photo_filepath')].split("**");

        this.arr_photo_comment = res[0][tableFieldsArr.indexOf('arr_photo_comment')].split("**");

        this.arr_photo_datetime = res[0][tableFieldsArr.indexOf('arr_photo_datetime')].split("**");

        this.arr_photo_width_height = res[0][tableFieldsArr.indexOf('arr_photo_width_height')].split("**");

        if(this.arr_photo_filepath.length==1 && this.arr_photo_filepath[0]==''){
          this.arr_photo_filepath = [];
          this.arr_photo_comment = [];
          this.arr_photo_datetime = [];
          this.arr_photo_width_height = [];
        }

        // if (res[0][tableFieldsArr.indexOf('arr_photo_filepath')] !== '') {
        //
        // }
        // if (res[0][tableFieldsArr.indexOf('arr_photo_comment')] !== '') {
        //
        // }
        // if (res[0][tableFieldsArr.indexOf('arr_photo_datetime')] !== '') {
        //
        // }

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

        for (var j = 0; j < 3 - this.arr_sample_number.length;j++) {
          this.table_data_arr.push({
            sample_number: '',
            zuanjin_depth: '',
            diceng_describe: '',
            wuran_describe: '',
            caiyang_depth: ''
          })
        }

        this.alreadyUploadedImagesList = [];

        for(var x=0;x<this.arr_photo_filepath.length;x++)
        {
          let arrr = this.arr_photo_filepath[x].split("/");
          let imgName = arrr[arrr.length-1];
          this.alreadyUploadedImagesList.push({name:imgName,url:this.arr_photo_filepath[x],comment:this.arr_photo_comment[x],dt:this.arr_photo_datetime[x],width:this.arr_photo_width_height[x][0],height:this.arr_photo_width_height[x][1]})
        }

        this.initReadyOK();

      }).catch((error) => {

          console.log("encounter db access error")

        this.initStaticDataDemo();

        this.initReadyOK();

      });
      },

      openViewOneImage(index){

        this.imgSelfShowFlag = false;
        let selectOneObj = this.alreadyUploadedImagesList[index];
        this.currentShowImageIndex = index;
        this.ifShowImageFlag = true;
        this.currentShowImageFileName = selectOneObj.name;
        if(selectOneObj.dt != '' && selectOneObj.dt != null){
          //this.currentShowImageDateTime = '（照片拍摄时间：'+selectOneObj.dt+'）';
          this.currentShowImageDateTime = '（上传时间：'+selectOneObj.dt+'）';
        }else{
          this.currentShowImageDateTime = '';
        }

        this.currentShowImageURL = selectOneObj.url;
        this.currentShowImageComment = selectOneObj.comment;
        this.imgObj = new Image();
        this.imgObj.src = this.currentShowImageURL;
        this.imgObj.onload = this.getImageLoadedHandler
      },

      del_one_image(){
        this.alreadyUploadedImagesList.splice(this.currentShowImageIndex,1);

        console.log("this.alreadyUploadedImagesList.length=="+this.alreadyUploadedImagesList.length);

        this.ifShowImageFlag = false;
        //这里记得更新数据库
      },

      not_del_one_image(){

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

      saveFillInHandler(){
        //调用 py 程序保存到数据库表中
        this.insertOrUpdateSoilDrillTable();
      },

      handleChange(dv){
        this.record_date = dv;
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

        this.d("loadingEntityForEditSoilDrillRecord").style.left = (document.body.offsetWidth - this.d("loadingEntityForEditSoilDrillRecord").offsetWidth) / 2 + "px";

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
        this.neishen_signature222 = '陈总办公室222';

        this.record_date = "2018年7月16日";

        this.alreadyUploadedImagesList = [];

        this.alreadyUploadedImagesList.push({name:'abcdefg.jpg',url:'/static/0.jpg',comment:'土层表面纹理',dt:'2018-07-13 11:10'})
        this.alreadyUploadedImagesList.push({name:'uuuu1.jpg',url:'/static/1.jpg',comment:'13日白天阳光照射下的土',dt:'2018-07-15 15:27'})
        this.alreadyUploadedImagesList.push({name:'uuuu2.jpg',url:'/static/2.jpg',comment:'红桥区二号院土地',dt:'2018-07-14 18:11'})
        this.alreadyUploadedImagesList.push({name:'uuuu3.jpg',url:'/static/3.jpg',comment:'下雨过后的土壤',dt:'2018-07-09 20:10'})
        this.alreadyUploadedImagesList.push({name:'uuuu4.jpg',url:'/static/4.jpg',comment:'团队合作',dt:'2018-07-08 09:10'})
        this.alreadyUploadedImagesList.push({name:'uuuu5.jpg',url:'/static/5.jpg',comment:'砖红色的土层',dt:'2018-07-13 10:10'})

        this.table_data_arr = [];
        this.table_data_arr.push({sample_number: 'Y0021', zuanjin_depth: '21m', diceng_describe: '土质疏松，发黑，颗粒密度小',
          wuran_describe:'有不好的味道，黏糊糊的，估计已经变质一段时间',caiyang_depth:'37m'});
        this.table_data_arr.push({sample_number: 'Y0049', zuanjin_depth: '16m', diceng_describe: '土块很潮湿，浅黄色，长期被水浸泡，很软',
          wuran_describe:'未见污染，未见异样气味',caiyang_depth:'11m'});
        this.table_data_arr.push({sample_number: '', zuanjin_depth: '', diceng_describe: '',
          wuran_describe:'',caiyang_depth:''});

        for(var i=0;i<this.table_data_arr.length;i++)
        {
          this.arr_sample_number.push(this.table_data_arr[i].sample_number);
          this.arr_zuanjin_depth.push(this.table_data_arr[i].zuanjin_depth);
          this.arr_diceng_describe.push(this.table_data_arr[i].diceng_describe);
          this.arr_wuran_describe.push(this.table_data_arr[i].wuran_describe);
          this.arr_caiyang_depth.push(this.table_data_arr[i].caiyang_depth);
        }

        this.record_person_name = '朱小雨';

        this.neishen_signature = '陈总办公室';
        this.neishen_signature222 = '陈总办公室222';

      },

      insertOrUpdateSoilDrillTable(){
        let params = new URLSearchParams();

        let operateTableActionStr;

        if(this.currentRecordId != 0){
          params.append('record_id', this.currentRecordId);
          operateTableActionStr = '/update_soil_drill_table';
        } else {
          operateTableActionStr = '/insert_soil_drill_table';
          this.first_submit_time = new Date().Format("yyyy-MM-dd hh:mm");
        }

        this.latest_save_time = new Date().Format("yyyy-MM-dd hh:mm");

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

        this.arr_photo_filepath = [];
        this.arr_photo_comment = [];
        this.arr_photo_datetime = [];
        this.arr_photo_width_height = [];

        for(let i=0;i<this.alreadyUploadedImagesList.length;i++)
        {
          this.arr_photo_filepath.push(this.alreadyUploadedImagesList[i].url);
          this.arr_photo_comment.push(this.alreadyUploadedImagesList[i].comment);
          this.arr_photo_datetime.push(this.alreadyUploadedImagesList[i].dt);
          this.arr_photo_width_height.push([this.alreadyUploadedImagesList[i].width,this.alreadyUploadedImagesList[i].height]);
        }

        params.append('record_table_name', this.record_table_name);
        params.append('record_person_name', this.record_person_name);
        params.append('record_date', this.record_date == ''?'（未填写）':this.record_date);
        params.append('first_submit_time', this.first_submit_time);
        params.append('latest_save_time', this.latest_save_time);
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
        params.append('arr_photo_filepath', this.arr_photo_filepath.join("**"));
        params.append('arr_photo_comment', this.arr_photo_comment.join("**"));
        params.append('arr_photo_datetime', this.arr_photo_datetime.join("**"));
        params.append('arr_photo_width_height', JSON.stringify(this.arr_photo_width_height));
        params.append('photos_collection', '{}');

        this.axios({

          method: 'post',
          url: 'http://huankepy.neuseer.cn' + operateTableActionStr,
          data: params

        }).then((res) => {

          if(this.$store.state.currentSelectedRecordID != 0){

            //保存已有记录

          } else {

            //新建记录

            if(res.data.result > 0)
            {

              this.$store.state.currentSelectedRecordID = res.data.result;

              this.currentRecordId = res.data.result;

            }

          }

          alert('保存成功，点击确定查看');

          this.$router.push(`/view_soil_drill_record/${this.currentRecordId}`);

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

  .m-modelHintWords {
    font-family: "Microsoft YaHei";
    font-size: 16px;
  }

  .input-newTemplateNameTB {
    box-sizing: border-box;
    text-align: center;
    font-size: 14px;
    height: 35px;
    border-radius: 4px;
    border: 1px solid #c8cccf;
    color: #6a6f77;
    -web-kit-appearance: none;
    -moz-appearance: none;
    display: inline-block;
    outline: 0;
    text-decoration: none;
    width: 100%;
  }

  .m-input-template-name-box {
    margin: 0 auto;
  }

  .vertical-center-modal {
    align-items: center;
    justify-content: center;
  }

  .m-popup-modal{
    font-size:14px;
  }

  #fillInContent {
    clear:both;
    position: relative;
    width: 760px;
    height: auto;
    margin: auto;
  }

  #loadingEntityForEditSoilDrillRecord{
    position:fixed;
    top:190px;
  }

  #currentFillInStatusHintContainer{
    position:relative;
    float:right;
    font-size:16px;
  }

  #record_table_nameContainer{
    position:relative;
    float:left;
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
    right:40px;
  }

</style>

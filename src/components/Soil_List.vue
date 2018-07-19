<template>
    <div id="soil_list">

      <Breadcrumb style="text-align: left; margin-left:130px;margin-bottom:-40px;" separator=">">
        <BreadcrumbItem to="/">首页</BreadcrumbItem>
        <BreadcrumbItem to="/soil_entrance">土壤类记录表</BreadcrumbItem>
        <BreadcrumbItem to="/soil_list/0">{{latestBreadHere}}</BreadcrumbItem>
      </Breadcrumb>

      <div id="zhuankong_title">
        {{latestBreadHere}}
      </div>
      <br>
      <br>
      <div id="soilList" v-show="!ifShowLoadingNowFlag && table_data_arr.length>0">
        <Table size="large" ref="recordTable" border :width="tableRealWidth" :style="'left:'+tableLeftEdge+'px;'"
               :columns="table_column_arr"
               :data="table_data_arr"></Table>
      </div>

      <div id="delBtn" :style="'margin-left:'+tableLeftEdge+'px;'" v-show="!ifShowLoadingNowFlag && table_data_arr.length>0">
        <Button @click="readyForDelRecords">删除记录</Button>
        <div id="createBtn" :style="'position:relative;display:inline-block;float:right;right:'+tableLeftEdge+'px;'">
          <Button @click="createOneNewRecord">创建新记录</Button>
        </div>
      </div>

      <div id="noRecordHint" v-show="!ifShowLoadingNowFlag && table_data_arr.length==0">（暂无记录）</div>

      <br>
      <br>
      <br>

      <div id="createBtnTwin" v-show="!ifShowLoadingNowFlag && table_data_arr.length==0"><Button
        @click="createOneNewRecord">创建新记录</Button></div>

      <Modal
        v-model="showDelPopupBesureBoxFlag"
        width="400"
        title="温馨提示"
        @on-ok="ok_del"
        @on-cancel="cancel_del">
        <p class="m-popup-modal">{{hintIFDelOneOrSomeRecordsWord}}</p>
      </Modal>


      <Modal
        v-model="ifCreateOneNewRecordFlag"
        title="新建一个采样记录"
        width="360"
        class="vertical-center-modal"
        @on-ok="createRecord"
        @on-cancel="cancelCreateRecordQuit">
        <div class="m-input-record-name-box">
          <div><input type="text" placeholder="请输入记录名字..." id="newRecordNameTB" class="input-newRecordNameTB"
                      onfocus="this.placeholder='';"
                      onblur="this.value==''?this.placeholder='请输入记录名字...':this.placeholder='';"></div>
        </div>
      </Modal>

      <circleLoading id="loadingEntityForSoilList" v-show="ifShowLoadingNowFlag"></circleLoading>

    </div>
</template>

<script>
    export default {
      name: "soil_list",

      data() {
        return {
          ifShowLoadingNowFlag: true,
          table_column_arr: [],
          table_data_arr: [],
          tableLeftEdge: 10,
          tableRealWidth:983,
          showDelPopupBesureBoxFlag:false,
          hintIFDelOneOrSomeRecordsWord:'',
          ifCreateOneNewRecordFlag:false,
          recordsList:[],
          latestBreadHere:''
        }
      },
      mounted: function ()
      {

        this.soilTableTypeIndex = Number(this.$route.params.id);

        if(this.soilTableTypeIndex == 0){
          this.latestBreadHere = '电子土壤钻孔记录表';
        }else if(this.soilTableTypeIndex == 1){
          this.latestBreadHere = '电子土壤样品采集现场记录表';
        }

        this.table_column_arr = [];
        this.table_column_arr.push({type:'selection',width:50,align: 'center'});
        this.table_column_arr.push({title:'记录名称',key:'name',width:350,align: 'left',render: (h, params) => {
          return h('span', {
            domProps: {
              innerHTML: params.row.name,
              title:'点击查看详情'
            },
            style: {
              cursor: "pointer",
              color: "#007FFF"
            },
            on: {
              click: () => {
                  this.viewOneRecord(`${params.row._index}`);
              }
            }
          })
        }});

        this.table_column_arr.push({title:'创建记录的时间',key:'create_dt',width:200,align: 'center'});
        this.table_column_arr.push({title:'记录人',key:'person',width:100,align: 'center'});
        this.table_column_arr.push({title:'照片',key:'photo',width:80,align: 'center'});
        this.table_column_arr.push({title:'最新编辑的时间',key:'edit_dt',width:200,align: 'center'});


        this.rearrangeUIAfterResizeShowArea();

        this.requestDBForBasicData();

        //setTimeout(this.initReadyOK,1000);

        //setTimeout(this.rearrangeUIAfterResizeShowArea,2000)
      },

      methods: {

        /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
        echoParent() {
          this.rearrangeUIAfterResizeShowArea();
        }
        ,

        initStaticDataDemo(){
          this.table_data_arr = [];
          this.table_data_arr.push({name: '红桥区二号院实地勘测', create_dt: '2018-07-05 15:30', person: '朱小雨',
            photo:'有',edit_dt:'2018-07-05 18:06',id:1001});
          this.table_data_arr.push({name: '邕江支流拐弯处108号口岸附近采样', create_dt: '2018-07-07 14:00', person: '聂佳琳', photo:'无',edit_dt:'2018-07-07 17:21',id:1002});
          this.table_data_arr.push({name: '龙湖工业园C区土壤采点', create_dt: '2018-07-09 11:00', person: '张卫', photo:'有',edit_dt:'2018-07-10 2:10',id:1003});

        },

        requestDBForBasicData(){

          this.table_data_arr = [];

          let params = new URLSearchParams();
          params.append('username','');

          this.axios({
            method: 'post',
            url: 'http://datestpy.neuseer.cn/select_soil_drill_table',
            data:params

          }).then((res) => {

            if(res.data.result == '[]')
            {

              //
            }else {

              let receiveData = JSON.parse(res.data.result);

              let rlen = receiveData.length;

              let tableFieldsArr = ['id', 'record_table_name', 'record_person_name', 'record_date', 'first_submit_time', 'latest_save_time', 'neishen_signature', 'dikuai_name', 'dikuai_code', 'budian_person', 'budian_date', 'caiyang_date', 'caiyang_person', 'weather_info', 'dianwei_number', 'jingdu', 'weidu', 'caiyang_site', 'drill_person_name', 'drill_person_contact', 'drill_depth', 'drill_diameter', 'drill_method', 'drill_machine_model', 'chujian_water_level', 'zhikong_depth', 'arr_sample_number', 'arr_zuanjin_depth', 'arr_diceng_describe', 'arr_wuran_describe', 'arr_caiyang_depth'];


              for (var i = 0; i < rlen; i++) {

                this.table_data_arr.push({
                  name: receiveData[i][tableFieldsArr.indexOf('record_table_name')],
                  create_dt: receiveData[i][tableFieldsArr.indexOf('first_submit_time')],
                  person: receiveData[i][tableFieldsArr.indexOf('record_person_name')],
                  photo: '无',
                  edit_dt: receiveData[i][tableFieldsArr.indexOf('latest_save_time')],
                  id: receiveData[i][tableFieldsArr.indexOf('id')]
                });

              }

            }

            this.initReadyOK();

          }).catch((error) => {

            console.log("access py error: " + error);

            this.initStaticDataDemo();

            this.initReadyOK();

          });
        },

        ok_del(){
          this.execDeleteRecordHandler();
        },

        cancel_del(){

        },

        initReadyOK()
        {
          this.ifShowLoadingNowFlag = false;
        },


        viewOneRecord(index)
        {
          let recordID = this.table_data_arr[index].id;

          this.$store.state.currentSelectedRecordID = recordID;

          console.log("recordID="+recordID);
          if(this.soilTableTypeIndex == 0)
          {
            this.$router.push(`/view_soil_drill_record/${recordID}`);
          } else if(this.soilTableTypeIndex == 1){
            alert("查看电子土壤样品采集现场记录表的某一记录：稍后开放")
            //this.$router.push(`/view_soil_drill_record/${recordID}`);
          }
        },

        execDeleteRecordHandler()
        {

          for (var i = 0; i < this.$refs.recordTable.getSelection().length; i++) {

            let params = new URLSearchParams();

            params.append('record_id', this.$refs.recordTable.getSelection()[i].id);

            this.axios({
              method: 'post',
              url: 'http://datestpy.neuseer.cn/delete_soil_drill_record',
              data: params
            }).then((res) => {

              alert("删除记录成功！");

              this.requestDBForBasicData();

            }).catch((error) => {

            });
          }

        },

        readyForDelRecords(){

          if(this.$refs.recordTable.getSelection().length==0){
              alert('请勾选至少一条记录')
          } else {
            if(this.$refs.recordTable.getSelection().length == 1){
              this.hintIFDelOneOrSomeRecordsWord = '确定要删除该条记录吗？'
            } else if(this.$refs.recordTable.getSelection().length > 1){
              this.hintIFDelOneOrSomeRecordsWord = '确定要删除这几条记录吗？'
            }
            this.showDelPopupBesureBoxFlag = true;
          }

        },

        createOneNewRecord(){
          this.ifCreateOneNewRecordFlag = true;
        },

        rearrangeUIAfterResizeShowArea() {

          this.tableLeftEdge = (this.$store.state.coreBlockAreaWidth - this.tableRealWidth) / 2;

          this.d("loadingEntityForSoilList").style.left = (document.body.offsetWidth - this.d("loadingEntityForSoilList").offsetWidth) / 2 + "px";

        },

        createRecord() {

          let str = this.d("newRecordNameTB").value.trim();

          if (str == "") {

            this.$Message.info('请输入有效的采样记录名称');

            setTimeout(this.atOnceReShow, 0);

          } else if (this.repeatNameJudgement(str)) {

            this.$Message.info('该名称已存在，请重新命名');

            //this.waitReadyForCreateNewFla = false;

            setTimeout(this.atOnceReShow, 0);

          } else if(escape(str).indexOf("%u") !=-1 && str.length>20) {

            alert("采样记录命名请不要超过20个汉字的长度");

            setTimeout(this.atOnceReShow, 0);

          } else if(str.length>30){

            alert("采样记录命名请不要超过30个英文半角字符的长度");

            setTimeout(this.atOnceReShow, 0);

          } else {

            this.$store.state.recordName = str;

            this.$store.state.currentSelectedRecordID = 0;

            if(this.soilTableTypeIndex == 0)
            {
              this.$router.push('/edit_soil_drill_record/0');

            }else if(this.soilTableTypeIndex == 1){
              alert('“电子土壤样品采集现场记录表” 暂时不开放填写');
              //this.$router.push('/edit_soil_sample_gather_record');
            }

          }

        }
        ,

        repeatNameJudgement(nameStr) {

          this.recordsList[0] = {};
          this.recordsList[0].record_name = "e";
          let len = this.recordsList.length;
          let repeatFlag = false;
          for (var i = 0; i < len; i++) {
            if (this.recordsList[i].record_name != null && this.recordsList[i].record_name == nameStr) {
              repeatFlag = true;
              break;
            }
          }
          return repeatFlag;
        },

        atOnceReShow(){
          this.ifCreateOneNewRecordFlag = true;
        },

        cancelCreateRecordQuit() {
          //this.$Message.info('Clicked cancel');
        }
        ,

      }
    }
</script>

<style scoped>

  .input-newRecordNameTB {
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

  #loadingEntityForSoilList{
    position:fixed;
    top:190px;
  }

  #zhuankong_title
  {
    position:relative;
    width: auto;
    text-align: center;
    margin-top:80px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #noRecordHint{
    text-align: center;
  }

  #createBtnTwin{
    text-align: center;
  }

  .m-input-record-name-box {
    margin: 0 auto;
  }

  .vertical-center-modal {
    align-items: center;
    justify-content: center;
  }

  #delBtn{
    position:relative;
    width:auto;
    text-align:left;
    margin-top:40px;
  }

  .m-popup-modal{
    font-size:14px;
  }
</style>

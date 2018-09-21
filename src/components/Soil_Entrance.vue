<template>
    <div id="soil_entrance">

      <Breadcrumb style="text-align: left; margin-left:130px;margin-bottom:-40px;" separator=">">
        <BreadcrumbItem to="/">首页</BreadcrumbItem>
        <BreadcrumbItem>土壤类记录表</BreadcrumbItem>

      </Breadcrumb>

      <div id="title">
        土壤类记录表
      </div>
      <div id="itemsList" v-show="!ifShowLoadingNowFlag">
        <Table size="large" :width="tableRealWidth" border :style="'left:'+tableLeftEdge+'px;'" :columns="table_column_arr"
               :data="table_data_arr"></Table>
      </div>

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


      <circleLoading id="loadingEntityForSoilEntrance" v-show="ifShowLoadingNowFlag"></circleLoading>

    </div>
</template>

<script>
  export default
  {
    name: "soil_entrance",

    data() {
      return {
        ifShowLoadingNowFlag: true,
        table_column_arr: [],
        table_data_arr: [],
        tableLeftEdge:10,
        ifCreateOneNewRecordFlag:false,
        recordsList:[],
        tableRealWidth:502,
        soilTableTypeIndex:-1,
        currentRequestTable:'',
        soil_drill_table_record_amount:3,
        soil_sample_gather_table_record_amount:1
      }
    },
    mounted: function ()
    {
      this.table_column_arr = [];
      this.table_column_arr.push({title:'表名',key:'tableName',width:300,align: 'left',render: (h, params) => {
        return h('span', {
          domProps: {
            innerHTML: params.row.tableName,
            title:'查看历史记录'
          },
          style: {
            cursor: "pointer",
            color: "#007FFF"
          },
          on: {
            click: () => {
              this.wantToViewRecords(`${params.row._index}`);
          }
        }
      })
    }});
      this.table_column_arr.push({title:'已填写',key:'amount',width:100,align: 'center'});
      this.table_column_arr.push({title:'快速新建',key:'new',width:100,align: 'center',render: (h, params) => {
        return h('div', [
          h('Icon', {
            props: {
              type: 'ios-create-outline',
              size: 22
            },
            style: {
              cursor: 'pointer'
            },
            on:{
              'click':()=>{
                  this.wantToNewOneRecord(`${params.row._index}`);
              }
            }
          })
        ]);
      }});

      this.requestPointedSoilTableRecordAmount("DC_Soil_Drill");

      //setTimeout(this.initReadyOK,1000);

      this.rearrangeUIAfterResizeShowArea();
    },
    methods:{

      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      }
      ,

      initReadyOK()
      {
        this.ifShowLoadingNowFlag = false;

        this.table_data_arr = [];

        this.table_data_arr.push({tableName:'电子土壤钻孔记录表',amount:this.soil_drill_table_record_amount,new:'write'});

        this.table_data_arr.push({tableName:'电子土壤样品采集现场记录表',amount:this.soil_sample_gather_table_record_amount,new:'write'});
      },

      wantToViewRecords(index){

        if(index == 0)
        {
          this.$router.push(`/soil_list/${index}`);
        } else {

          alert('“电子土壤样品采集现场记录表” 暂时不开放查看存档记录');
        }

      },

      wantToNewOneRecord(index){
        this.soilTableTypeIndex = index;
        if(this.soilTableTypeIndex > 0)
        {
          alert('“电子土壤样品采集现场记录表” 暂时不开放填写');

        }else{
          this.ifCreateOneNewRecordFlag = true;
        }

      },

      rearrangeUIAfterResizeShowArea() {

        this.tableLeftEdge = (this.$store.state.coreBlockAreaWidth - this.tableRealWidth) /2;

        this.d("title").style.width = this.$store.state.coreBlockAreaWidth + "px";

        this.d("loadingEntityForSoilEntrance").style.left = (document.body.offsetWidth - this.d("loadingEntityForSoilEntrance").offsetWidth) / 2 + "px";

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

          this.$store.state.recordName = str

          this.$store.state.currentSelectedRecordID = 0;

          this.$router.push('/edit_soil_drill_record/0');

        }

      }
      ,
      cancelCreateRecordQuit() {
        //this.$Message.info('Clicked cancel');
      }
      ,

      atOnceReShow(){
        this.ifCreateOneNewRecordFlag = true;
      },

      repeatNameJudgement(nameStr) {

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

      requestPointedSoilTableRecordAmount(tableName){

        this.currentRequestTable = tableName;

        let params = new URLSearchParams();

        params.append('which_one_table',tableName);

        this.axios({
          method: 'post',
          url: 'http://huankepy.neuseer.cn/get_one_soil_table_record_amount',
          data:params

        }).then((res) => {

          let recoreAmount = Number(JSON.parse(res.data.result));

          if (this.currentRequestTable == "DC_Soil_Drill") {
            this.soil_drill_table_record_amount = recoreAmount;
            this.requestPointedSoilTableRecordAmount("DC_Soil_Sample_Gather");
          } else if (this.currentRequestTable == "DC_Soil_Sample_Gather") {
            this.soil_sample_gather_table_record_amount = recoreAmount;
            this.initReadyOK();
          }

        }).catch((error) => {

            console.log("access py error: " + error);

            this.initReadyOK();

        });
      },

    }
  }
</script>

<style scoped>

  #title {
    text-align: center;
    margin-top: 70px;
    margin-bottom: 30px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #loadingEntityForSoilEntrance{
    position:fixed;
    top:190px;
  }

  .vertical-center-modal {
    align-items: center;
    justify-content: center;
  }

  .m-input-record-name-box {
    margin: 0 auto;
  }

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

</style>

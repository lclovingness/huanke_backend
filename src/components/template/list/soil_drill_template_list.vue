<template>
  <div id="soil_list">

    <Breadcrumb style="text-align: left; margin-left:100px;margin-bottom:-40px;" separator=">">
      <BreadcrumbItem to="/">首页</BreadcrumbItem>
      <BreadcrumbItem to="/soil_entrance">土壤类记录表</BreadcrumbItem>
      <BreadcrumbItem to="/soil_list/0">{{latestBreadHere}}</BreadcrumbItem>
      <BreadcrumbItem to="/template/list/soil_drill_template_list/0">模板列表</BreadcrumbItem>
    </Breadcrumb>

    <div id="zhuankong_title">
      {{latestBreadHere}}的模板列表
    </div>
    <br>
    <br>
    <div id="soilList" v-show="!ifShowLoadingNowFlag && table_data_arr.length>0">
      <Table size="large" ref="templateTable" border :width="tableRealWidth" :style="'left:'+tableLeftEdge+'px;'"
             :columns="table_column_arr"
             :data="table_data_arr"></Table>
    </div>

    <div id="delBtn" :style="'margin-left:'+tableLeftEdge+'px;'"
         v-show="!ifShowLoadingNowFlag && table_data_arr.length>0">
      <Button @click="readyForDelTemplates">删除模板</Button>
      <div id="createBtn" :style="'position:relative;display:inline-block;float:right;right:'+tableLeftEdge+'px;'">
        <Button @click="createOneNewTemplate">创建新模板</Button>
      </div>
    </div>

    <div id="noTemplateHint" v-show="!ifShowLoadingNowFlag && table_data_arr.length==0">（暂无模板）</div>

    <br>
    <br>
    <br>

    <div id="createBtnTwin" v-show="!ifShowLoadingNowFlag && table_data_arr.length==0">
      <Button
        @click="createOneNewTemplate">创建新模板
      </Button>
    </div>

    <Modal
      v-model="showDelPopupBesureBoxFlag"
      width="400"
      title="温馨提示"
      @on-ok="ok_del"
      @on-cancel="cancel_del">
      <p class="m-popup-modal">{{hintIFDelOneOrSomeTemplatesWord}}</p>
    </Modal>

    <Modal
      v-model="ifCreateOneNewTemplateFlag"
      title="新建一个模板"
      width="360"
      class="vertical-center-modal"
      @on-ok="createTemplate"
      @on-cancel="cancelCreateTemplateQuit">
      <div class="m-input-record-name-box">
        <div><input type="text" placeholder="请输入模板名称..." id="newTemplateNameTB" class="input-newTemplateNameTB"
                    onfocus="this.placeholder='';"
                    onblur="this.value==''?this.placeholder='请输入模板名称...':this.placeholder='';"></div>
      </div>
    </Modal>

    <circleLoading id="loadingEntityForSoilList" v-show="ifShowLoadingNowFlag"></circleLoading>

  </div>
</template>

<script>
  export default {
    name: "soil_drill_template_list",

    data() {
      return {
        ifShowLoadingNowFlag: true,
        table_column_arr: [],
        table_data_arr: [],
        tableLeftEdge: 10,
        tableRealWidth: 602,
        showDelPopupBesureBoxFlag: false,
        hintIFDelOneOrSomeTemplatesWord: '',
        ifCreateOneNewTemplateFlag: false,
        recordsList: [],
        latestBreadHere: ''
      }
    },
    mounted: function () {

      this.soilTableTypeIndex = Number(this.$route.params.id);

      if (this.soilTableTypeIndex == 0) {
        this.latestBreadHere = '电子土壤钻孔记录表';
      } else if (this.soilTableTypeIndex == 1) {
        this.latestBreadHere = '电子土壤样品采集现场记录表';
      }

      this.table_column_arr = [];
      this.table_column_arr.push({type: 'selection', width: 50, align: 'center'});
      this.table_column_arr.push({title: '模板名称', key: 'name', width: 350, align: 'left',
        render: (h, params) => {
          return h('span', {
            domProps: {
              innerHTML: params.row.name,
              title: '点击查看'
            },
            style: {
              cursor: "pointer",
              color: "#007FFF"
            },
            on: {
              click: () => {

                this.viewOneTemplate(`${params.row._index}`);
              }
            }
          })
        }
      });

      this.table_column_arr.push({title: '模板更新的时间', key: 'update_template_time', width: 200, align: 'center'});

      this.rearrangeUIAfterResizeShowArea();

      this.requestDBForBasicData();

      //setTimeout(this.initReadyOK,1000);

      //setTimeout(this.rearrangeUIAfterResizeShowArea,2000)
    },

    methods: {

      readyForShowTemplateList() {
        this.$router.push('/template/list/soil_drill_template_list');
      },

      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      }
      ,

      requestDBForBasicData() {

        this.table_data_arr = [];

        let params = new URLSearchParams();
        params.append('username', '');

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

              this.table_data_arr.push({
                name: receiveData[i][tableFieldsArr.indexOf('template_table_name')],
                update_template_time: receiveData[i][tableFieldsArr.indexOf('update_date_time')],
                id: receiveData[i][tableFieldsArr.indexOf('id')],
              });

            }

          }

          this.initReadyOK();

        }).catch((error) => {

          console.log("access py error: " + error);

          this.initReadyOK();

        });
      },

      judgeIFHavePhoto(v) {
        let arr = v.split("**");
        if (v == '') {
          return '无';
        } else if (v.length == 1 && v[0] == '') {
          return '无';
        } else {
          return '有';
        }

      },

      ok_del() {
        this.execDeleteTemplateHandler();
      },

      cancel_del() {

      },

      initReadyOK() {
        this.ifShowLoadingNowFlag = false;
      },

      viewOneTemplate(index) {
        this.$store.state.currentSelectedTemplateID = this.table_data_arr[index].id;

        if (this.soilTableTypeIndex == 0) {
          this.$router.push(`/template/view_soil_drill_template/${this.table_data_arr[index].id}`);
        } else if (this.soilTableTypeIndex == 1) {
          alert("查看电子土壤样品采集现场记录表的某一记录：稍后开放")
          //this.$router.push(`/view_soil_drill_record/${recordID}`);
        }
      },

      execDeleteTemplateHandler() {

        let arr = this.$refs.templateTable.getSelection();

        this.deletedAmount = 0;

        for (var i = 0; i < arr.length; i++) {

          let params = new URLSearchParams();

          params.append('template_id', arr[i].id);

          this.axios({
            method: 'post',
            url: 'http://huankepy.neuseer.cn/delete_soil_drill_template',
            data: params
          }).then((res) => {

            this.deletedAmount++;

            if(this.deletedAmount == arr.length)
            {
              alert("删除模板成功！");
              this.requestDBForBasicData();
            }
          });
        }
      },

      readyForDelTemplates() {

        if (this.$refs.templateTable.getSelection().length == 0) {
          alert('请勾选相应的模板')
        } else {
          if (this.$refs.templateTable.getSelection().length == 1) {
            this.hintIFDelOneOrSomeTemplatesWord = '确定要删除该模板吗？'
          } else if (this.$refs.templateTable.getSelection().length > 1) {
            this.hintIFDelOneOrSomeTemplatesWord = '确定要删除这几个模板吗？'
          }
          this.showDelPopupBesureBoxFlag = true;
        }

      },

      createOneNewTemplate() {
        this.ifCreateOneNewTemplateFlag = true;
      },

      rearrangeUIAfterResizeShowArea() {

        this.d("zhuankong_title").style.width = document.body.offsetWidth + "px";

        this.d("createBtnTwin").style.width = document.body.offsetWidth + "px";

        this.d("noTemplateHint").style.width = document.body.offsetWidth + "px";

        this.tableLeftEdge = (this.$store.state.coreBlockAreaWidth - this.tableRealWidth) / 2;

        this.d("loadingEntityForSoilList").style.left = (document.body.offsetWidth - this.d("loadingEntityForSoilList").offsetWidth) / 2 + "px";

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

          if (this.soilTableTypeIndex == 0) {
            this.$router.push('/template/compile_soil_drill_template/0');

          } else if (this.soilTableTypeIndex == 1) {
            alert('“电子土壤样品采集现场记录表的模板” 暂时不开放创建');
            //this.$router.push('/edit_soil_sample_gather_record');
          }

        }

      },

      repeatNameJudgement(nameStr) {

        let len = this.table_data_arr.length;
        let repeatFlag = false;
        for (var i = 0; i < len; i++) {
          if (this.table_data_arr[i].name == nameStr) {
            repeatFlag = true;
            break;
          }
        }
        return repeatFlag;
      },

      atOnceReShow() {
        this.ifCreateOneNewTemplateFlag = true;
      },

      cancelCreateTemplateQuit() {
        //this.$Message.info('Clicked cancel');
      },

    }
  }
</script>

<style>

  .ivu-table-cell {
    display: block !important;
  }
</style>

<style scoped>

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

  #loadingEntityForSoilList {
    position: fixed;
    top: 190px;
  }

  #zhuankong_title {
    position: relative;
    text-align: center;
    margin-top: 80px;
    font-family: "Helvetica Neue", "Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #noTemplateHint {
    text-align: center;
  }

  #createBtnTwin {
    text-align: center;
  }

  .m-input-record-name-box {
    margin: 0 auto;
  }

  .vertical-center-modal {
    align-items: center;
    justify-content: center;
  }

  #delBtn {
    position: relative;
    text-align: left;
    margin-top: 40px;
  }

  .m-popup-modal {
    font-size: 14px;
  }

  #templateRegion {
    position: absolute;
    float: right;
    top: 60px;
    right: 60px;
  }

</style>

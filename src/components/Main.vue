<template>

  <div id="main_entrance">

    <div id="title">
      主分类入口
    </div>

    <div id="bigEntranceButtonsContainer" :style="'left:'+bigEntranceBtnsContainerLeftEdge+'px'">

      <span class="m-left-big-btn">
       <Card style="width:220px;height:180px;">
          <div class="m-bigCard" @click="jumpSoilEntrance">
              <img src="/static/soil.png">
              <br>
              <span style="font-size:28px;font-weight:bold">土壤</span>
          </div>
       </Card>
      </span>

      <span class="m-right-big-btn">
        <Card style="width:220px;height:180px;">
          <div class="m-bigCard" @click="jumpWaterEntrance">
              <img src="/static/water.png">
              <br>
              <span style="font-size:28px;font-weight:bold">地下水</span>
          </div>
       </Card>
      </span>

    </div>

  </div>

</template>

<script>

  export default {

    name: 'Main',

    data() {
      return {
        bigEntranceBtnsContainerLeftEdge:-1
      }
    },

    mounted: function () {

      this.rearrangeUIAfterResizeShowArea();

    },
    methods: {
      /*响应父级调用的通信方法，父级可通过调用此方法，通知子路由做一些什么事件*/
      echoParent() {
        this.rearrangeUIAfterResizeShowArea();
      }
      ,
      rearrangeUIAfterResizeShowArea() {

        this.bigEntranceBtnsContainerLeftEdge = (this.$store.state.coreBlockAreaWidth - 800) /2;

      },

      jumpSoilEntrance(){
        this.$router.push('/soil_entrance');
      },

      jumpWaterEntrance(){
        this.$router.push('/water_entrance');
      },
    }
  }

</script>



<style>
  #bigEntranceButtonsContainer .ivu-card-body {
    background-color: aquamarine !important;
  }

  #bigEntranceButtonsContainer .ivu-card-body:hover{
    background-color: bisque !important;
  }
</style>

<style scoped>

  #title {
    width: 100%;
    text-align: center;
    margin-top: 70px;
    margin-bottom: 50px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 28px;
    font-weight: bold;
  }

  #bigEntranceButtonsContainer
  {
    position: relative;
    text-align:center;
    width: 800px;
    height: 600px;
    cursor:pointer;
  }

  .m-left-big-btn {
    float: left;
    margin-left: 100px
  }

  .m-right-big-btn {
    float: right;
    margin-right: 100px;
  }

  .m-bigCard{
    margin-top:10px;
    margin-bottom:10px;
  }

</style>

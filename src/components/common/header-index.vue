<template>
  <div class="header1">
    <div class="logo">
      <img src="../../assets/img/logo.svg">
      环科中心 · 土壤和地下水采样数据记录管理系统
    </div>
    <div id="adminInfo">
      版本号：1.0  （请由管理员操作）
    </div>
    <!--<div id="twoMainEntrance" v-show="comingSoonFlag">-->
      <!--<span id="projectEntrance" :class="{'u-entrance-highlight': whereAddressIndex==0}" @click="goWhere(0)">土壤</span>-->
      <!--<span id="taskEntrance" :class="{'u-entrance-highlight': whereAddressIndex==1}" @click="goWhere(1)">地下水</span>-->
    <!--</div>-->
  </div>
</template>
<style lang="less" scoped>

  #adminInfo{
    position:fixed;
    float:right;
    top:0;
    right:50px;
    height:40px;
    line-height:40px;
    font-size:12px;
    /*color: #d6d6d6;*/
    color: rgba(255,255,255,0.60);
    z-index:1000;
    cursor:pointer;
  }

  #twoMainEntrance{
    position:fixed;
    float:left;
    top:0;
    left:320px;
    height:40px;
    line-height:40px;
    font-size:12px;
    /*color: #d6d6d6;*/
    color: rgba(255,255,255,0.60);
    z-index:1000;
    cursor:pointer;
  }

  #projectEntrance{
    width:114px;
    padding:11px 21px;
  }

  #projectEntrance:hover{
    color: rgba(255,255,255,1);
    transition: color 0.5s ease-in 0s;
  }

  #taskEntrance{
    width:114px;
    padding:11px 21px;
  }

  #taskEntrance:hover{
    color: rgba(255,255,255,1);
    transition: color 0.5s ease-in 0s;
  }

  #globalConfig{
    width:114px;
    padding:11px 21px;
  }

  #globalConfig:hover{
    color: rgba(255,255,255,1);
    transition: color 0.5s ease-in 0s;
  }

  .u-entrance-highlight{
    background: #1B202A;
    color:#fff;
    font-weight: bold;
  }

  .iot-menu-horizontal {
    height: 40px;
    line-height: 40px;
  }

  .iot-menu-dark {
    background: #282F3E;
  }

  .vertical-center-modal {
    align-items: center;
    justify-content: center;
  }

  .u-besuredelsty {
    font-family: "Microsoft YaHei";
    font-size: 14px;
  }

  .usersty {
    font-size: 12px;
    cursor: default;
    pointer-events: none;
  }

  .logoutsty {
    margin-top: -2px;
    vertical-align: middle;
  }

  .logo {
    position:fixed;
    float:left;
    top:0;
    left:30px;
    color: #ffffff;
    font-size: 12px;
    height:40px;
    line-height:40px;
    cursor:default;
    z-index:999;
    img {
      width: 18px;
      position: relative;
      top: 3px;
      right: 4px;
    }
  }

  .header1 {
    position:fixed;
    top:0;
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    background-color:#282F3E;
    width:100%;
    height:40px;

    .login {
      float: right;
      margin-right: 10px;
      color: #fff;
      line-height: 40px;
    }
  }


</style>
<script>

  export default {
    data() {
      return {
        comingSoonFlag:true,
        path: '',
        username: '',
        hintTabWaringModel:false,
        whereAddressIndex:null,
        tempAddIndex:-1
      };
    },
    watch: {
      '$route.path': function () {

      },

    },
    mounted: function () {

      if(window.localStorage.currentPath == "tasks")
      {

        this.whereAddressIndex = 1;

      }else{

        this.whereAddressIndex = 0;
      }
    },
    methods: {

      goWhere(n){

        if(this.$route.path == "/open")
        {
          this.hintTabWaringModel = true;
          this.tempAddIndex = n;
          return;
        }

        if(this.$route.path.indexOf("refactor-task")>-1)
        {
          if(n==0)
          {
            this.$store.state.nextPlace = "/projects";
          }else{
            this.$store.state.nextPlace = "/tasks";

          }
          return;
        }

        this.whereAddressIndex = n;

        if(n==0)
        {
          this.$router.push("/soil_entrance");
        }else if(n==1){
          this.$router.push("/water_entrance");
        }else if(n==2){
          this.$router.push("/config");
        }
      },

    }
  };
</script>

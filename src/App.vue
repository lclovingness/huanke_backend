<template>
  <div id="app">
    <div class="wrapper">
      <header-index class="header-index" ref="headerIndex"></header-index>
      <div id="cc" class="main clearfix">
        <div class="con-main">
          <router-view ref="sonCore"></router-view>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

  import HeaderIndex from '@/components/common/header-index.vue';

  export default {
    name: 'App',
    components: {
      'header-index': HeaderIndex
    },
    mounted: function () {
      this.$router.push('/');

      this.trackWindowOnResize();

      window.onresize = this.trackWindowOnResize;

    },
    methods: {
      trackWindowOnResize() {

        this.$store.state.coreBlockAreaWidth = document.body.offsetWidth;

        //console.log("coreBlockAreaWidth=="+this.$store.state.coreBlockAreaWidth)
        if(this.$refs.sonCore != null){
          this.$refs.sonCore.echoParent();
        }
      },
    }
  }

</script>

<style>

  @import "./assets/less/reset.less";

  html{
    overflow-y:scroll;
  }

  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }

  .header-index{
    z-index:10;
  }

  .con-main{
    z-index:9;
  }
</style>

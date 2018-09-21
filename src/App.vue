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
      //this.$router.push('/');

      this.neceInit();

      this.trackWindowOnResize();

      window.onresize = this.trackWindowOnResize;

    },
    methods: {

      neceInit(){

        this.$store.state.soil_drill_template_table_fields = ['id', 'template_table_name', 'update_date_time', 'record_person_name', 'neishen_signature', 'dikuai_name', 'dikuai_code', 'budian_person', 'budian_date', 'caiyang_date', 'caiyang_person', 'weather_info', 'dianwei_number', 'jingdu', 'weidu', 'caiyang_site', 'drill_person_name', 'drill_person_contact', 'drill_depth', 'drill_diameter', 'drill_method', 'drill_machine_model', 'chujian_water_level', 'zhikong_depth', 'arr_sample_number', 'arr_zuanjin_depth', 'arr_diceng_describe', 'arr_wuran_describe', 'arr_caiyang_depth'];
      },

      trackWindowOnResize() {

        this.$store.state.coreBlockAreaWidth = document.body.offsetWidth;

        if(this.$refs.sonCore != null)
        {
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

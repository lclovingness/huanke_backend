import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import SoilEntrance from '@/components/Soil_Entrance'
import WaterEntrance from '@/components/Water_Entrance'
import SoilList from '@/components/Soil_List'
import EditSoilDrillRecord from '@/components/edit_soil_drill_record'
import ViewSoilDrillRecord from '@/components/view_soil_drill_record'
import CompileSoilDrillTemplate from '@/components/template/compile_soil_drill_template'
import ViewSoilDrillTemplate from '@/components/template/view_soil_drill_template'
import SoilDrillTemplateList from '@/components/template/list/soil_drill_template_list'
import PhotosSoilDrillPage from '@/components/photos_soil_drill_page'

Vue.use(Router)

export default new Router({
  mode:'hash', // 默认是 hash ，网页的URL会带 # 号；如果是 history ，则不带 # 号 。 参见：https://router.vuejs.org/zh-cn/essentials/history-mode.html
  routes: [
    {
      path: '/',
      redirect:'/main'
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/soil_entrance',
      name: 'SoilEntrance',
      component: SoilEntrance
    },
    {
      path: '/water_entrance',
      name: 'WaterEntrance',
      component: WaterEntrance
    },
    {
      path: '/soil_list/:id',
      name: 'SoilList',
      component: SoilList
    },
    {
      path: '/edit_soil_drill_record/:id',  // 填写电子土壤钻孔记录表（可以是新建，也可以是修改保存过的记录）
      name: 'EditSoilDrillRecord',
      component: EditSoilDrillRecord
    },
    {
      path: '/view_soil_drill_record/:id',  // 查看保存过的电子土壤钻孔记录表
      name: 'ViewSoilDrillRecord',
      component: ViewSoilDrillRecord
    },
    {
      path: '/template/compile_soil_drill_template/:id',  // 编写电子土壤钻孔记录表模板
      name: 'CompileSoilDrillTemplate',
      component: CompileSoilDrillTemplate
    },
    {
      path: '/template/list/soil_drill_template_list/:id',  // 电子土壤钻孔记录表模板列表显示
      name: 'SoilDrillTemplateList',
      component: SoilDrillTemplateList
    },
    {
      path: '/template/view_soil_drill_template/:id',  // 查看电子土壤钻孔记录表模板
      name: 'ViewSoilDrillTemplate',
      component: ViewSoilDrillTemplate
    }
    ,
    {
      path: '/photos_soil_drill_page/:id',  // 电子土壤钻孔记录的照片集合打印页
      name: 'PhotosSoilDrillPage',
      component: PhotosSoilDrillPage
    }

  ]
})

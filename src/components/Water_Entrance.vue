<template>
    <div id="soil_entrance">
      <div id="title">
       地下水类采样记录表
      </div>
      <br>
      <div id="itemsList">
        ( 展现形式和土壤类的一致，请先看土壤的，试用确认好后，会统一优化 ）
      </div>
      <div id="tempBtn">
        <Button type="primary" size="large" @click="$router.back(-1)">返回</Button>
      </div>
    </div>
</template>

<script>
    export default {
        name: "water_entrance"
    }
</script>

<style scoped>
  #title {
    width: 100%;
    text-align: center;
    margin-top: 70px;
    margin-bottom: 10px;
    font-family: "Helvetica Neue","Microsoft YaHei";
    font-size: 20px;
    font-weight: bold;
  }

  #itemsList{
    width:100%;
    font-size:14px;
  }

  #tempBtn{
    margin-top:50px;
  }
</style>

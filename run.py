# -*- coding:utf8 -*-

from flask import Flask, request, jsonify
import json,pymysql
from flask_cors import *

app = Flask(__name__)

CORS(app, supports_credentials=True)


@app.route('/select_soil_drill_table',methods=['POST'])
def selectSoilDrillTable():

  try:
    conn=pymysql.connect(host="172.30.209.34",user="csdemo",passwd="csdemo2018",db="ctestdb",port="3306",charset="utf8")

    cur=conn.cursor()

    sql_select ='select * from DC_Soil_Drill order by id desc'

    cur.execute(sql_select)

    result = cur.fetchall()

    return jsonify(result=json.dumps(result,ensure_ascii=False))

    cur.close()

  except  Exception :print("select DC_Soil_Drill data error access")

  finally:
    conn.close()


@app.route('/insert_soil_drill_table',methods=['POST'])
def insertSoilDrillTable():
  record_table_name = request.form.get('record_table_name')
  record_person_name	 = request.form.get('record_person_name')
  record_date = request.form.get('record_date')
  first_submit_time = request.form.get('first_submit_time')
  latest_save_time = request.form.get('latest_save_time')
  neishen_signature = request.form.get('neishen_signature')
  dikuai_name = request.form.get('dikuai_name')
  dikuai_code = request.form.get('dikuai_code')
  budian_person = request.form.get('budian_person')
  budian_date = request.form.get('budian_date')
  caiyang_date = request.form.get('caiyang_date')
  caiyang_person = request.form.get('caiyang_person')
  weather_info = request.form.get('weather_info')
  dianwei_number = request.form.get('dianwei_number')
  jingdu = request.form.get('jingdu')
  weidu = request.form.get('weidu')
  caiyang_site = request.form.get('caiyang_site')
  drill_person_name = request.form.get('drill_person_name')
  drill_person_contact = request.form.get('drill_person_contact')
  drill_depth = request.form.get('drill_depth')
  drill_diameter = request.form.get('drill_diameter')
  drill_method = request.form.get('drill_method')
  drill_machine_model = request.form.get('drill_machine_model')
  chujian_water_level = request.form.get('chujian_water_level')
  zhikong_depth = request.form.get('zhikong_depth')
  arr_sample_number = request.form.get('arr_sample_number')
  arr_zhuanjin_depth = request.form.get('arr_zhuanjin_depth')
  arr_diceng_describe = request.form.get('arr_diceng_describe')
  arr_wuran_describe = request.form.get('arr_wuran_describe')
  arr_caiyang_depth = request.form.get('arr_caiyang_depth')
  arr_photo_filepath = request.form.get('arr_photo_filepath')
  arr_photo_comment = request.form.get('arr_photo_comment')
  arr_photo_datetime = request.form.get('arr_photo_datetime')


  conn=pymysql.connect(host="172.30.209.34",user="csdemo",passwd="csdemo2018",db="ctestdb",port="3306",charset="utf8")

  cur=conn.cursor()

  sql_insert ="insert into DC_Soil_Drill values(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

  cur.execute(sql_insert,(record_table_name,record_person_name,record_date,first_submit_time,latest_save_time,
                          neishen_signature,dikuai_name,dikuai_code,budian_person,budian_date,caiyang_date,
                          caiyang_person,weather_info,dianwei_number,jingdu,weidu,caiyang_site,drill_person_name,
                          drill_person_contact,drill_depth,drill_diameter,drill_method,drill_machine_model,
                          chujian_water_level,zhikong_depth,arr_sample_number,arr_zhuanjin_depth,arr_diceng_describe,
                          arr_wuran_describe,arr_caiyang_depth,arr_photo_filepath,arr_photo_comment,arr_photo_datetime))

  newid=conn.insert_id()

  conn.commit()

  return jsonify(result=newid)
  #return jsonify(result="insert ok")

  cur.close()

  conn.close()

@app.route('/update_soil_drill_table',methods=['POST'])
def updateSoilDrillTable():
  record_id = request.form.get('record_id')
  record_table_name = request.form.get('record_table_name')
  record_person_name	 = request.form.get('record_person_name')
  record_date = request.form.get('record_date')
  first_submit_time = request.form.get('first_submit_time')
  latest_save_time = request.form.get('latest_save_time')
  neishen_signature = request.form.get('neishen_signature')
  dikuai_name = request.form.get('dikuai_name')
  dikuai_code = request.form.get('dikuai_code')
  budian_person = request.form.get('budian_person')
  budian_date = request.form.get('budian_date')
  caiyang_date = request.form.get('caiyang_date')
  caiyang_person = request.form.get('caiyang_person')
  weather_info = request.form.get('weather_info')
  dianwei_number = request.form.get('dianwei_number')
  jingdu = request.form.get('jingdu')
  weidu = request.form.get('weidu')
  caiyang_site = request.form.get('caiyang_site')
  drill_person_name = request.form.get('drill_person_name')
  drill_person_contact = request.form.get('drill_person_contact')
  drill_depth = request.form.get('drill_depth')
  drill_diameter = request.form.get('drill_diameter')
  drill_method = request.form.get('drill_method')
  drill_machine_model = request.form.get('drill_machine_model')
  chujian_water_level = request.form.get('chujian_water_level')
  zhikong_depth = request.form.get('zhikong_depth')
  arr_sample_number = request.form.get('arr_sample_number')
  arr_zhuanjin_depth = request.form.get('arr_zhuanjin_depth')
  arr_diceng_describe = request.form.get('arr_diceng_describe')
  arr_wuran_describe = request.form.get('arr_wuran_describe')
  arr_caiyang_depth = request.form.get('arr_caiyang_depth')
  arr_photo_filepath = request.form.get('arr_photo_filepath')
  arr_photo_comment = request.form.get('arr_photo_comment')
  arr_photo_datetime = request.form.get('arr_photo_datetime')

  conn=pymysql.connect(host="172.30.209.34",user="csdemo",passwd="csdemo2018",db="ctestdb",port="3306",charset="utf8")

  cur=conn.cursor()

  sql_update ="update DC_Soil_Drill set record_table_name=%s,record_person_name=%s,record_date=%s,first_submit_time=%s,latest_save_time=%s,neishen_signature=%s,dikuai_name=%s,dikuai_code=%s,budian_person=%s,budian_date=%s,caiyang_date=%s,caiyang_person=%s,weather_info=%s,dianwei_number=%s,jingdu=%s,weidu=%s,caiyang_site=%s,drill_person_name=%s,drill_person_contact=%s,drill_depth=%s,drill_diameter=%s,drill_method=%s,drill_machine_model=%s,chujian_water_level=%s,zhikong_depth=%s,arr_sample_number=%s,arr_zhuanjin_depth=%s,arr_diceng_describe=%s,arr_wuran_describe=%s,arr_caiyang_depth=%s,arr_photo_filepath=%s,arr_photo_comment=%s,arr_photo_datetime=%s where id=%s"

  try:
    cur.execute(sql_update,(record_table_name,record_person_name,record_date,first_submit_time,latest_save_time,
                            neishen_signature,dikuai_name,dikuai_code,budian_person,budian_date,caiyang_date,
                            caiyang_person,weather_info,dianwei_number,jingdu,weidu,caiyang_site,drill_person_name,
                            drill_person_contact,drill_depth,drill_diameter,drill_method,drill_machine_model,
                            chujian_water_level,zhikong_depth,arr_sample_number,arr_zhuanjin_depth,arr_diceng_describe,
                            arr_wuran_describe,arr_caiyang_depth,arr_photo_filepath,arr_photo_comment,arr_photo_datetime,record_id))

    conn.commit()

    return jsonify(result="update task ok")

  except Exception :

    return jsonify(str(traceback.format_exc()))

  cur.close()

  conn.close()


@app.route('/delete_soil_drill_table',methods=['POST'])
def deleteSoilDrillTable():

  idsCollection = request.form.get('idsCollection')
  #idsCollection = '128,129'
  idsCollection = idsCollection.split(',')
  idsCollection = tuple([int(s) for s in idsCollection])

  try:
    conn=pymysql.connect(host="172.30.209.34",user="csdemo",passwd="csdemo2018",db="ctestdb",port="3306",charset="utf8")

    cur=conn.cursor()

    sql_delete ="delete from DC_Soil_Drill where id in "+str(idsCollection)

    cur.execute(sql_delete)

    conn.commit()

    return jsonify(result="delete ok")

    cur.close()

  except  Exception :print("delete DC_Soil_Drill happened some errors")

  finally:
    conn.close()


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)

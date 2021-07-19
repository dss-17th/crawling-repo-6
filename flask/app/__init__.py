from flask import Flask, render_template, jsonify, request
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from flask import *
from app.config import Config

# database에 접근
db= pymysql.connect(host='35.223.152.188',
                     port=3306,
                     user='root',
                     passwd='dss',
                     charset='utf8')

app = Flask(__name__)
app.config.from_object(Config)


# from app.items.mysql_zigbang import Zigbang, ZigbangApt, zigbang_db, zigbang_apt_db
# from app.items.mysql_kakao import KaKaoApt, KaKaoOneroom, KaKaoOfficetel, KaKaoVilla
# from app.items.mysql_kakao import kakao_apt_db, kakao_oneroom_db, kakao_officetel_db, kakao_villa_db


@app.route("/")
def index():
    return render_template("map.html")

@app.route('/apt_listup', methods=['GET'])
def apt_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select name, dong, lat, lng, image, rent_min, rent_max, rent_avg, sales_min, sales_max, sales_avg from zigbang_apt;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    
    return jsonify({'result': 'success', 'apt_list': result})

@app.route('/villa_listup', methods=['GET'])
def villa_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select address, lat, lng, images_thumbnail, deposit, rent from zigbang_villa;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    
    return jsonify({'result': 'success', 'villa_list': result})

@app.route('/oneroom_listup', methods=['GET'])
def oneroom_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select address, lat, lng, images_thumbnail, deposit, rent, sales_title from zigbang_oneroom;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    
    return jsonify({'result': 'success', 'oneroom_list': result})

@app.route('/officetel_listup', methods=['GET'])
def officetel_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select address, lat, lng, images_thumbnail, deposit, rent, sales_title from zigbang_officetel;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    
    return jsonify({'result': 'success', 'officetel_list': result})


@app.route("/api")
def show_map():
    result = {"code": 200}
    cate = request.values.get("type")
    result['datas'] = {}
    result['datas']['type'] = cate

    if cate != "아파트":
        datas = Zigbang.query.filter_by(category=f"{cate}").all()
    else:
        datas = ZigbangApt.query.filter_by(category=f"{cate}").all()

    result['datas']['lat'] = [data.lat for data in datas]
    result['datas']['lng'] = [data.lng for data in datas]
    result['datas']['name'] = [data.name for data in datas]
    result['datas']['p'] = [data.p for data in datas]

    print(result)

    return jsonify(result)
    return render_template("test.html", data=result)


@app.route("/home/map")
def test():
    return render_template("test.html")

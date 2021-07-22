from flask import Flask, render_template, jsonify, request
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from flask import *
from app.config import info

# database에 접근
db = pymysql.connect(host=info["IP"],
                     port=3306,
                     user=info["USER"],
                     passwd=info["PASSWORD"],
                     charset="utf8")

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

    sql_ls = ['use data','select name, dong, lat, lng, image, rent_min, rent_max, rent_avg, sales_min, sales_max, sales_avg, MT1, CS2, PS3, SC4, AC5, PK6, OL7, SW8, BK9, CT1, AG2, PO3, AT4, AD5, FD6, CE7, HP8, PM9  from zigbang_apt;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    position = []
    for i in result:
        position.append({'lat' : i[2],'lng' : i[3]})

    print(position)
    
    return jsonify({'result': 'success', 'apt_list': result, 'positions' : position})

# MT1	대형마트
# CS2	편의점
# PS3	어린이집, 유치원
# SC4	학교
# AC5	학원
# PK6	주차장
# OL7	주유소, 충전소
# SW8	지하철역
# BK9	은행
# CT1	문화시설
# AG2	중개업소
# PO3	공공기관
# AT4	관광명소
# AD5	숙박
# FD6	음식점
# CE7	카페
# HP8	병원
# PM9   약국
# MT1, CS2, PS3, SC4, AC5, PK6, OL7, SW8, BK9, CT1, AG2, PO3, AT4, AD5, FD6, CE7, HP8, PM9

@app.route('/villa_listup', methods=['GET'])
def villa_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select sales_type, lat, lng, deposit, MT1, CS2, PS3, SC4, AC5, PK6, OL7, SW8, BK9, CT1, AG2, PO3, AT4, AD5, FD6, CE7, HP8, PM9  from zigbang_villa;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    
    return jsonify({'result': 'success', 'villa_list': result})

@app.route('/oneroom_listup', methods=['GET'])
def oneroom_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select sales_type, lat, lng, deposit, MT1, CS2, PS3, SC4, AC5, PK6, OL7, SW8, BK9, CT1, AG2, PO3, AT4, AD5, FD6, CE7, HP8, PM9, rent from zigbang_oneroom;']

    for sql in sql_ls:
        cursor.execute(sql)
    
    result= cursor.fetchall()
    
    return jsonify({'result': 'success', 'oneroom_list': result})

@app.route('/officetel_listup', methods=['GET'])
def officetel_listup():
    cursor= db.cursor()

    sql_ls = ['use data','select sales_type, lat, lng, deposit, MT1, CS2, PS3, SC4, AC5, PK6, OL7, SW8, BK9, CT1, AG2, PO3, AT4, AD5, FD6, CE7, HP8, PM9, rent from zigbang_officetel;']

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



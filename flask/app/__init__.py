import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from flask import *
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)


from app.items.mysql_zigbang import Zigbang, ZigbangApt, zigbang_db, zigbang_apt_db
from app.items.mysql_kakao import KaKaoApt, KaKaoOneroom, KaKaoOfficetel, KaKaoVilla
from app.items.mysql_kakao import kakao_apt_db, kakao_oneroom_db, kakao_officetel_db, kakao_villa_db


@app.route("/home")
def index():
    return render_template("index2.html")


@app.route("/home/map")
def show_map():
    result = {"code": 200}
    cate = request.values.get("type")
    print(cate)
    result["type"] = cate

    if cate != "아파트":
        result['datas'] = Zigbang.query.filter_by(category=f"{cate}")
    else:
        result['datas'] = ZigbangApt.query.filter_by(category=f"{cate}")
    

    return jsonify(result)

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

from flask import *
from app.config import Config


app = Flask(__name__)
app.config.from_object(Config)


from app.items.mysql_zigbang import Zigbang, ZigbangApt, zigbang_db, zigbang_apt_db
from app.items.mysql.kakao import KaKaoApt, KaKaoOneroom, KaKaoOfficetel, KaKaoVilla
from app.items.mysql.kakao import kakao_apt_db, kakao_oneroom_db, kakao_officetel_db, kakao_villa_db


@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/home/map")
def show_map():
    result = {"code": 200}
    type = request.values.get("type")
    result["type"] = type

    if type != "아파트":
        curr_db = zigbang_db
    else:
        curr_db = zigbang_apt_db

    datas = curr_db.query.filter_by(category=f"{type}")

    return jsonify(datas)

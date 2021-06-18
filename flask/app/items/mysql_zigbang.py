from app import app
from flask_sqlalchemy import SQLAlchemy


zigbang_db = SQLAlchemy(app)
zigbang_apt_db = SQLAlchemy(app)

# zigbang oneroom, officetel, villa
class Zigbang(zigbang_db.Model):

    __tablename__ = "zigbang"

    index = zigbang_db.Column(zigbang_db.Integer, primary_key=True)
    address = zigbang_db.Column(zigbang_db.Text)
    address1 = zigbang_db.Column(zigbang_db.Text)
    address2 = zigbang_db.Column(zigbang_db.Integer)
    address3 = zigbang_db.Column(zigbang_db.Integer)
    building_floor = zigbang_db.Column(zigbang_db.Text)
    deposit = zigbang_db.Column(zigbang_db.Integer)
    floor = zigbang_db.Column(zigbang_db.Text)
    floor_string = zigbang_db.Column(zigbang_db.Text)
    images_thumbnail = zigbang_db.Column(zigbang_db.Text)
    is_first_movein = zigbang_db.Column(zigbang_db.Integer)
    is_new = zigbang_db.Column(zigbang_db.Integer)
    is_zzim = zigbang_db.Column(zigbang_db.Integer)
    item_id = zigbang_db.Column(zigbang_db.Integer)
    manage_cost = zigbang_db.Column(zigbang_db.Text)
    reg_date = zigbang_db.Column(zigbang_db.Text)
    rent = zigbang_db.Column(zigbang_db.Integer)
    room_type = zigbang_db.Column(zigbang_db.Text)
    room_type_title = zigbang_db.Column(zigbang_db.Integer)
    sales_title = zigbang_db.Column(zigbang_db.Text)
    sales_type = zigbang_db.Column(zigbang_db.Text)
    section_type = zigbang_db.Column(zigbang_db.Integer)
    service_type = zigbang_db.Column(zigbang_db.Text)
    size_m2 = zigbang_db.Column(zigbang_db.Integer)
    status = zigbang_db.Column(zigbang_db.Integer)
    공급면적_m2 = zigbang_db.Column(zigbang_db.Integer)
    공급면적_p = zigbang_db.Column(zigbang_db.Text)
    전용면적_m2 = zigbang_db.Column(zigbang_db.Integer)
    전용면적_p = zigbang_db.Column(zigbang_db.Text)
    lat = zigbang_db.Column(zigbang_db.Integer)
    lng = zigbang_db.Column(zigbang_db.Integer)
    category = zigbang_db.Column(zigbang_db.Text)

    def __init__(self, address, lat, lng, category):
        self.address = address
        self.lat = lat
        self.lng = lng
        self.category = category


# DB에 primary_key로 index 추가해야함
# zigbang apt
class ZigbangApt(zigbang_apt_db.Model):

    __tablename__ = "zigbang_apt"

    brand = zigbang_apt_db.Column(zigbang_apt_db.Text)
    buildDate = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    bunji = zigbang_apt_db.Column(zigbang_apt_db.Text)
    dong = zigbang_apt_db.Column(zigbang_apt_db.Text)
    gugun = zigbang_apt_db.Column(zigbang_apt_db.Text)
    households = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    id = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    image = zigbang_apt_db.Column(zigbang_apt_db.Text)
    isLargestRoomType = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    is후분양 = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    itemCnt = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    lat = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    lng = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    name = zigbang_apt_db.Column(zigbang_apt_db.Text)
    real_type = zigbang_apt_db.Column(zigbang_apt_db.Text)
    score = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    sido = zigbang_apt_db.Column(zigbang_apt_db.Text)
    transactionCnt = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    분양년월 = zigbang_apt_db.Column(zigbang_apt_db.Text)
    분양년월마커 = zigbang_apt_db.Column(zigbang_apt_db.Text)
    분양년월마커길이lv = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    사용승인일 = zigbang_apt_db.Column(zigbang_apt_db.Text)
    서비스구분 = zigbang_apt_db.Column(zigbang_apt_db.Text)
    register = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    online = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    rent_mim = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    rent_max = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    rent_avg = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    sales_min = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    sales_max = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    sales_avg = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    offer_min = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    offer_max = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    offer_avg = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    m2 = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    p = zigbang_apt_db.Column(zigbang_apt_db.Integer)
    category = zigbang_apt_db.Column(zigbang_apt_db.Text)

    def __init__(self, lat, lng, category):
        self.lat = lat
        self.lng = lng
        self.category = category


zigbang_db.create_all()
zigbang_apt_db.create_all()

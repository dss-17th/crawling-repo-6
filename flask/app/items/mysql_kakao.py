from app import app
from flask_sqlalchemy import SQLAlchemy

kakao_apt_db = SQLAlchemy(app)
kakao_oneroom_db = SQLAlchemy(app)
kakao_officetel_db = SQLAlchemy(app)
kakao_villa_db = SQLAlchemy(app)


# DB에 primary_key로 index 추가해야함
class KaKaoApt(kakao_apt_db.Model):

    __tablename__ = "apt"

    address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_code = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_name = kakao_apt_db.Column(kakao_apt_db.Text)
    distance = kakao_apt_db.Column(kakao_apt_db.Text)
    id = kakao_apt_db.Column(kakao_apt_db.Text)
    phone = kakao_apt_db.Column(kakao_apt_db.Text)
    place_name = kakao_apt_db.Column(kakao_apt_db.Text)
    place_url = kakao_apt_db.Column(kakao_apt_db.Text)
    road_address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    x = kakao_apt_db.Column(kakao_apt_db.Text)
    y = kakao_apt_db.Column(kakao_apt_db.Text)
    매물_lat = kakao_apt_db.Column(kakao_apt_db.Integer)
    매물_lng = kakao_apt_db.Column(kakao_apt_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


# DB에 primary_key로 index 추가해야함
class KaKaoOneroom(kakao_oneroom_db.Model):

    __tablename__ = "oneroom"

    address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_code = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_name = kakao_apt_db.Column(kakao_apt_db.Text)
    distance = kakao_apt_db.Column(kakao_apt_db.Text)
    id = kakao_apt_db.Column(kakao_apt_db.Text)
    phone = kakao_apt_db.Column(kakao_apt_db.Text)
    place_name = kakao_apt_db.Column(kakao_apt_db.Text)
    place_url = kakao_apt_db.Column(kakao_apt_db.Text)
    road_address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    x = kakao_apt_db.Column(kakao_apt_db.Text)
    y = kakao_apt_db.Column(kakao_apt_db.Text)
    매물_lat = kakao_apt_db.Column(kakao_apt_db.Integer)
    매물_lng = kakao_apt_db.Column(kakao_apt_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


# DB에 primary_key로 index 추가해야함
class KaKaoOfficetel(kakao_officetel_db.Model):

    __tablename__ = "officetel"

    address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_code = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_name = kakao_apt_db.Column(kakao_apt_db.Text)
    distance = kakao_apt_db.Column(kakao_apt_db.Text)
    id = kakao_apt_db.Column(kakao_apt_db.Text)
    phone = kakao_apt_db.Column(kakao_apt_db.Text)
    place_name = kakao_apt_db.Column(kakao_apt_db.Text)
    place_url = kakao_apt_db.Column(kakao_apt_db.Text)
    road_address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    x = kakao_apt_db.Column(kakao_apt_db.Text)
    y = kakao_apt_db.Column(kakao_apt_db.Text)
    매물_lat = kakao_apt_db.Column(kakao_apt_db.Integer)
    매물_lng = kakao_apt_db.Column(kakao_apt_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


# DB에 primary_key로 index 추가해야함
class KaKaoVilla(kakao_villa_db.Model):

    __tablename__ = "villa"

    address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_code = kakao_apt_db.Column(kakao_apt_db.Text)
    category_group_name = kakao_apt_db.Column(kakao_apt_db.Text)
    category_name = kakao_apt_db.Column(kakao_apt_db.Text)
    distance = kakao_apt_db.Column(kakao_apt_db.Text)
    id = kakao_apt_db.Column(kakao_apt_db.Text)
    phone = kakao_apt_db.Column(kakao_apt_db.Text)
    place_name = kakao_apt_db.Column(kakao_apt_db.Text)
    place_url = kakao_apt_db.Column(kakao_apt_db.Text)
    road_address_name = kakao_apt_db.Column(kakao_apt_db.Text)
    x = kakao_apt_db.Column(kakao_apt_db.Text)
    y = kakao_apt_db.Column(kakao_apt_db.Text)
    매물_lat = kakao_apt_db.Column(kakao_apt_db.Integer)
    매물_lng = kakao_apt_db.Column(kakao_apt_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


kakao_apt_db.create_all()
kakao_oneroom_db.create_all()
kakao_officetel_db.create_all()
kakao_villa_db.create_all()

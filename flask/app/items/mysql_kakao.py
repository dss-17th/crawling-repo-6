from app import app
from flask_sqlalchemy import SQLAlchemy


kakao_apt_db = SQLAlchemy(app)
kakao_oneroom_db = SQLAlchemy(app)
kakao_officetel_db = SQLAlchemy(app)
kakao_villa_db = SQLAlchemy(app)

class KaKaoApt(kakao_apt_db.Model):

    __tablename__ = "apt"

    index = kakao_apt_db.Column(kakao_apt_db.Integer, primary_key=True)
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


class KaKaoOneroom(kakao_oneroom_db.Model):

    __tablename__ = "oneroom"

    index = kakao_oneroom_db.Column(kakao_oneroom_db.Integer, primary_key=True)
    address_name =  kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    category_group_code = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    category_group_name = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    category_name = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    distance = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    id = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    phone = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    place_name = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    place_url = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    road_address_name = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    x = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    y = kakao_oneroom_db.Column(kakao_oneroom_db.Text)
    매물_lat = kakao_oneroom_db.Column(kakao_oneroom_db.Integer)
    매물_lng = kakao_oneroom_db.Column(kakao_oneroom_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


class KaKaoOfficetel(kakao_officetel_db.Model):

    __tablename__ = "officetel"

    index = kakao_officetel_db.Column(kakao_officetel_db.Integer, primary_key=True)
    address_name = kakao_officetel_db.Column(kakao_officetel_db.Text)
    category_group_code = kakao_officetel_db.Column(kakao_officetel_db.Text)
    category_group_name = kakao_officetel_db.Column(kakao_officetel_db.Text)
    category_name = kakao_officetel_db.Column(kakao_officetel_db.Text)
    distance = kakao_officetel_db.Column(kakao_officetel_db.Text)
    id = kakao_officetel_db.Column(kakao_officetel_db.Text)
    phone = kakao_officetel_db.Column(kakao_officetel_db.Text)
    place_name = kakao_officetel_db.Column(kakao_officetel_db.Text)
    place_url = kakao_officetel_db.Column(kakao_officetel_db.Text)
    road_address_name = kakao_officetel_db.Column(kakao_officetel_db.Text)
    x = kakao_officetel_db.Column(kakao_officetel_db.Text)
    y = kakao_officetel_db.Column(kakao_officetel_db.Text)
    매물_lat = kakao_officetel_db.Column(kakao_officetel_db.Integer)
    매물_lng = kakao_officetel_db.Column(kakao_officetel_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


class KaKaoVilla(kakao_villa_db.Model):

    __tablename__ = "villa"

    index = kakao_villa_db.Column(kakao_villa_db.Integer, primary_key=True)
    address_name = kakao_villa_db.Column(kakao_villa_db.Text)
    category_group_code = kakao_villa_db.Column(kakao_villa_db.Text)
    category_group_name = kakao_villa_db.Column(kakao_villa_db.Text)
    category_name = kakao_villa_db.Column(kakao_villa_db.Text)
    distance = kakao_villa_db.Column(kakao_villa_db.Text)
    id = kakao_villa_db.Column(kakao_villa_db.Text)
    phone = kakao_villa_db.Column(kakao_villa_db.Text)
    place_name = kakao_villa_db.Column(kakao_villa_db.Text)
    place_url = kakao_villa_db.Column(kakao_villa_db.Text)
    road_address_name = kakao_villa_db.Column(kakao_villa_db.Text)
    x = kakao_villa_db.Column(kakao_villa_db.Text)
    y = kakao_villa_db.Column(kakao_villa_db.Text)
    매물_lat = kakao_villa_db.Column(kakao_villa_db.Integer)
    매물_lng = kakao_villa_db.Column(kakao_villa_db.Integer)

    def __init__(self, category_name, place_name, x, y):
        self.category_name  = category_name
        self.place_name = place_name
        self.x = x
        self.y = y


kakao_apt_db.create_all()
kakao_oneroom_db.create_all()
kakao_officetel_db.create_all()
kakao_villa_db.create_all()

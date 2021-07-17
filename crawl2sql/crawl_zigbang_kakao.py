import geohash2
import pandas as pd
import requests
import configparser

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from sqlalchemy import create_engine

from module.kakao import kakao
from module.zigbang import SearchDatas


config = configparser.ConfigParser()
config.read("../../data.ini")
info = config["crawl"]
print("import done")

# SQL 서버연결
engine = create_engine(f'mysql+pymysql://{info["USER"]}:{info["PASSWORD"]}@{info["IP"]}/{info["DB"]}', encoding='utf-8')
conn = engine.connect()

# 서울시 광진구 위치정보를 가진 객체 생성
gwangjin = SearchDatas("서울시 광진구")


# 서울시 광진구 precision 5에 대한 매물 데이터 크롤링

# 직방 원룸에 대한 매물 데이터 수집
zigbang_oneroom = gwangjin.zigbang_oneroom()

# 직방 빌라에 대한 매물 데이터 수집
zigbang_villa = gwangjin.zigbang_villa()

# 직방 오피스텔에 대한 매물 데이터 수집
zigbang_officetel = gwangjin.zigbang_officetel()

# 직방 아파트에 대한 매물 데이터 수집
zigbang_apt = gwangjin.zigbang_apt()


# 카카오 API를 이용한 직방 매물 데이터에 대한 편의시설 정보 크롤링 and 직방 dataframe에 편의시설별 총 개수 컬럼 생성

# 직방 원룸 매물에 대한 편의시설 데이터 수집
kakao_oneroom = kakao(info["REST_API"], target=zigbang_oneroom)

# 직방 빌라에 대한 편의시설 데이터 수집
kakao_villa = kakao(info["REST_API"], target=zigbang_villa)

# 직방 오피스텔에 대한 편의시설 데이터 수집
kakao_officetel = kakao(info["REST_API"], target=zigbang_officetel)

# 직방 아파트에 대한 매물 데이터 수집
kakao_apt = kakao(info["REST_API"], target=zigbang_apt)


zigbang_datasets = {"zigbang_oneroom": zigbang_oneroom, "zigbang_villa": zigbang_villa, 
                    "zigbang_officetel": zigbang_officetel, "zigbang_apt": zigbang_apt}
kakao_datasets = {"oneroom": kakao_oneroom, "villa": kakao_villa, "officetel": kakao_officetel, "apt": kakao_apt}

# 직방 수집 데이터 전처리 후 DB에 저장
for name, dataset in zigbang_datasets.items():
    dataset = dataset.fillna(0)

    if name != "zigbang_apt":
        dataset = dataset.drop(["tags","title"], 1)

    dataset.to_sql(name=name, con=engine, if_exists='replace', index=False, chunksize=1000)


# 카카오 수집 데이터 전처리 후 DB에 저장
for name, dataset in kakao_datasets.items():
    dataset.to_sql(name=name, con=engine, if_exists="replace", index=False, chunksize=1000)
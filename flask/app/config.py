import configparser


config = configparser.ConfigParser()
config.read("../../data.ini")
info = config["crawl"]

class Config(object):
    TEMPLATES_AUTO_RELOAD = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'mysql://{info["USER"]}:{info["PASSWORD"]}@{info["IP"]}/{info["DB"]}'

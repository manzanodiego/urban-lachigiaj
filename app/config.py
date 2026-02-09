import os


class Config:

    SQLALCHEMY_DATABASE_URI = ("mysql+pymysql://root:1234@localhost/Sistema-Urbans")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
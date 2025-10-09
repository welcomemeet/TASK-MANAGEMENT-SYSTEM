import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = "your_secret_key_here"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Meet%402005@localhost/task_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

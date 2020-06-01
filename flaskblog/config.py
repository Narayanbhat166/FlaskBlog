import os

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT= 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_ID')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
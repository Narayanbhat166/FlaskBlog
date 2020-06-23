import os

class Config():
    SECRET_KEY = "52c9bffc0288f98ada7c4c08a002a947"
    # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT= 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('MAIL_ID')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
import os


class Config(object):
    DEBUG = True
    SECRET_KEY = 'Sarvesh@123'
    BOOTSTRAP_BTN_STYLE = 'btn px-4 btn-outline-success'

    APP_ID = os.getenv('APP_ID')
    APP_KEY = os.getenv('APP_KEY')

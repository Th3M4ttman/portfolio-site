# -*- coding: utf-8 -*-

import os

from .utils import INSTANCE_FOLDER_PATH


class BaseConfig(object):
    # Change these settings as per your needs

    PROJECT = "flaskstarter"
    PROJECT_NAME = "https://matt-harris-portfolio.herokuapp.com"
    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    BASE_URL = "https://matt-harris-portfolio.herokuapp.com"
    ADMIN_EMAILS = ['admin@flaskstarter.domain']

    DEBUG = False
    TESTING = False

    SECRET_KEY = 'always-change-this-secret-key-with-random-alpha-nums'


class DefaultConfig(BaseConfig):

    DEBUG = True

    # Flask-Sqlalchemy
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SQLITE for production
    SQLALCHEMY_DATABASE_URI = "sqlite:////" + os.path.abspath(os.path.dirname(os.path.dirname(__file__)))  + INSTANCE_FOLDER_PATH + '/db.sqlite'
    

    # POSTGRESQL for production
    #SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:pass@ip/dbname'

    # Flask-cache
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60

    # Flask-mail
    MAIL_DEBUG = False
    MAIL_SERVER = "smpt.gmail.com"  # something like 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # Keep these in instance folder or in env variables
    MAIL_USERNAME = "admin-mail@yourdomain-flaskstarter.domain"
    MAIL_PASSWORD = ""
    MAIL_DEFAULT_SENDER = MAIL_USERNAME

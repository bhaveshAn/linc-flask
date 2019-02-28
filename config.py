# -*- coding: utf-8 -*-
import os

from envparse import env

env.read_envfile()

basedir = os.path.abspath(os.path.dirname(__file__))

VERSION_NAME = '2.1.0-alpha.0'

LANGUAGES = {
    'en': 'English',
    'bn': 'Bengali/Bangla',
    'zh_Hans': 'Chinese (Simplified)',
    'zh_Hant': 'Chinese (Traditional)',
    'fr': 'French',
    'de': 'German',
    'id': 'Indonesian',
    'ko': 'Korean',
    'pl': 'Polish',
    'es': 'Spanish',
    'th': 'Thai',
    'vi': 'Vietnamese',
    'hi': 'Hindi',
    'ja': 'Japanese',
    'ru': 'Russian',
}


class Config(object):
    """
    The base configuration option. Contains the defaults.
    """

    DEBUG = True

    DEVELOPMENT = False
    STAGING = False
    PRODUCTION = False
    TESTING = False

    CACHING = False
    PROFILE = False
    SQLALCHEMY_RECORD_QUERIES = False

    FLASK_ADMIN_SWATCH = 'lumen'

    VERSION = VERSION_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ERROR_404_HELP = False
    CSRF_ENABLED = True
    SERVER_NAME = env('SERVER_NAME', default=None)
    CORS_HEADERS = 'Content-Type'
    SQLALCHEMY_DATABASE_URI = env('DATABASE_URL', default=None)
    SERVE_STATIC = env.bool('SERVE_STATIC', default=False)
    DATABASE_QUERY_TIMEOUT = 0.1
    ETAG = True

    if not SQLALCHEMY_DATABASE_URI:
        print('`DATABASE_URL` either not exported or empty')
        exit()

    BASE_DIR = basedir
    FORCE_SSL = os.getenv('FORCE_SSL', 'no') == 'yes'

    if SERVE_STATIC:
        UPLOADS_FOLDER = BASE_DIR + '/static/uploads/'
        TEMP_UPLOADS_FOLDER = BASE_DIR + '/static/uploads/temp/'
        UPLOAD_FOLDER = UPLOADS_FOLDER
        STATIC_URL = '/static/'
        STATIC_ROOT = 'staticfiles'
        STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

    if FORCE_SSL:
        PREFERRED_URL_SCHEME = 'https'


class ProductionConfig(Config):
    """
    The configuration for a production environment
    """

    MINIFY_PAGE = True
    PRODUCTION = True
    CACHING = True

    # if force on


class StagingConfig(ProductionConfig):
    """
    The configuration for a staging environment
    """

    PRODUCTION = False
    STAGING = True


class DevelopmentConfig(Config):
    """
    The configuration for a development environment
    """

    DEVELOPMENT = True
    DEBUG = True
    CACHING = True
    PROPOGATE_ERROR = True

    # Test database performance
    SQLALCHEMY_RECORD_QUERIES = True

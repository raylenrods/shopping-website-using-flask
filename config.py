class Config(object):
    DEBUG=False
    TESTING=False
    SECRET_KEY='edc774184b83dbff4383cac336c36955cbf049bf9a269dc1091d0cdfaf5db2d4'
    DB_NAME='Production'
    DB_USERNAME='root'
    DB_PASSWORD=''
    UPLOADS='/media/abhishek/data/Flask/Project-Structure/app/static/img/uploads/'
    SESSION_COOKIE_SECURE=True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/FlaskProject'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG=True
    DB_NAME='Development'
    DB_USERNAME='root'
    DB_PASSWORD=''
    UPLOADS='/media/abhishek/data/Flask/Project-Structure-APP/app/static/img/uploads/'
    SESSION_COOKIE_SECURE=False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/FlaskProject'
    SQLALCHEMY_TRACK_MODIFICATIONS=True

class TestingConfig(Config):
    TESTING=True
    DB_NAME='Development'
    DB_USERNAME='root'
    DB_PASSWORD=''
    SESSION_COOKIE_SECURE=False
    UPLOADS='/media/abhishek/data/Flask/Project-Structure-APP/app/static/img/uploads/'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/FlaskProject'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
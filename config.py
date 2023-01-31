#Archivo que se encarga de gestionar las configuraciones de la web-app
class Config():
    DEBUG = True
    TESTING = True

    #Configuracion de la base de datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@192.168.100.6:3306/Techos_VerdesTest'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@127.0.0.1:3306/Techos_VerdesTest'

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True   
    TESTING = True
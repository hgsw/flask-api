DIALECT = "mysql"
DRIVER = "pymysql"
HOST = "localhost"
PORT = "3306"
USERNAME = "root"
PASSWORD = "123456"
DATABASE = "ginger"

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(
    DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE
)
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "fguaui3437vdfsbv29dv7hsbhou"
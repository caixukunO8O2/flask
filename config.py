SECRET_KEY = "keleyaojiabing"

# 数据库的配置信息
HOSTNAME = 'localhost'
PORT     = '3306'
DATABASE = 'qa'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "488876859@qq.com"
MAIL_PASSWORD = "fspxgasqjnzmcadf"
MAIL_DEFAULT_SENDER = "488876859@qq.com"

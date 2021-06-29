
class Dev:
    ENV = 'development'
    DEBUG = True

    # 配置SQLALCHEMY数据库连接及特征
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@116.62.193.152:3306/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 可扩展 兼容性问题
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 回收资源时自动关闭
    SQLALCHEMY_ECHO = True  # 显示SQL

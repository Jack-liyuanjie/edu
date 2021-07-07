from flask import render_template, request, redirect, url_for
from flask_script import Manager

from mainapp import app
from mainapp.views import user_v, logger_v
from models.user import db, User
from utils import cache


# 钩子函数
@app.before_request
def check_login():
    app.logger.info(request.path + '被访问了')
    if request.path not in ['/user/login',
                            '/log','/selflog']:
        # 判断request中是否包含token
        # 验证token是否有效
        token = request.cookies.get('token')
        if not token:
            return redirect(url_for('userBlue.login'))
        else:
            user_id = cache.get_user_id(token)
            if not user_id:
                return redirect(url_for('userBlue.login'))


@app.route('/create_db')
def create_database():
    db.create_all()
    return "创建数据库中的所有模型表成功"


@app.route('/drop_db')
def drop_database():
    db.drop_all()
    return "删除数据库中的所有模型表成功"


@app.route('/selflog')
def selflog():
    return "自己的日志文件喔"


@app.route('/')
def index():
    # 获取用户登录信息
    token = request.cookies.get('token')
    user_id = cache.get_user_id(token)
    user = User.query.get(int(user_id))
    return render_template('index.html', user=user)


if __name__ == '__main__':
    # 将蓝图注册到app中
    app.register_blueprint(user_v.blue, url_prefix='/user')
    app.register_blueprint(logger_v.blue)

    # 初始化数据库
    db.init_app(app)

    manager = Manager(app)
    manager.run()

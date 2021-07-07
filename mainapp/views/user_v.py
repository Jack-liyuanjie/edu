import os.path
import uuid
from datetime import datetime, timedelta
from flask import Blueprint, redirect, jsonify
from flask import request, render_template


from werkzeug.datastructures import FileStorage

import settings
from models import db
from models.user import User
from utils import crypy, cache

blue = Blueprint('userBlue', __name__)


@blue.route('/logout', methods=['GET'])
def logout():
    # 先删除redis中的token
    token = request.cookies.get('token')
    cache.clear_token(token)
    # 再删除cookie
    resp = redirect('/user/login')
    resp.delete_cookie('token')


@blue.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        phone = request.form.get('phone')
        passwd = request.form.get('passwd')

        login_user = User.query.filter(User.phone == phone,
                                       User.auth_key == crypy.pwd(passwd)).one()  # 特别注意filter后面的这个值one

        if login_user:
            # 登录成功
            # 生成token
            token = uuid.uuid4().hex
            resp = redirect('/')
            resp.set_cookie('token', token, expires=(datetime.now() + timedelta(days=3)))

            # 将token添加到redis，token-user_id
            cache.save_token(token, login_user.id)
            return resp
        else:
            message = '查无此用户'

    return render_template('user/login1.html', msg=message)


@blue.route('/upload', methods=['POST'])
def upload_photo():
    upload_file: FileStorage = request.files.get('photo')

    filename = uuid.uuid4().hex+os.path.splitext(upload_file.filename)[-1]
    filepath = os.path.join(settings.USER_DIR, filename)
    upload_file.save(filepath)

    user = User.query.get(cache.get_user_id(request.cookies.get('token')))
    # 任务1：删除之前的用户头像
    user.photo = 'user/' + filename
    db.session.commit()
    return jsonify({
        'msg': '上传成功',
        'path': 'user/'+filename
    })

# @blue.route('/modify', methods=['GET','POST'])
# def modify():
#     token = request.cookies.get('token')
#     user_id = cache.get_user_id(token)
#
#     # 任务一：优化登录用户的相关信息存在redis中（缓存）
#     user = User.query.get(int(user_id))
#
#     msg = ''
#     if request.method == 'POST':
#         # 头像上传
#         # 获取上传的文件
#         # user_phonto必须和前端请求中的文件字段保持一致
#         upload_file:FileStorage = request.files.get('user')
#         print('文件名：',upload_file.filename)
#         print('文件类别：', upload_file.content_type)
#         # 验证是否为图片
#         if not upload_file.content_type.startswith('image/*')
#             msg = '只支持图片上传'
#         else:
#             # 保存图片
#             filename = uuid.uuid4().hex + os.path.splitext(upload_file)
#             filepath = os.path.join(settings.USER_DIR, fi)
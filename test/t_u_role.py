from mainapp import app
from models.user import User, Role, QX, user_role, db
from utils import crypy


def add_user():
    u1 = User()
    u1.phone = '13267886101'
    u1.auth_key = crypy.pwd('000000')
    u1.nick_name = 'Jake'

    db.session.add(u1)
    print('add数据之前的User-Id:', u1.id)

    db.session.commit()
    print('add数据之后的User-Id:', u1.id)


def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')
    # 批量添加
    db.session.add_all((r1, r2))
    db.session.commit()
    print(r1.id, r2.id)


def add_user_role():
    # 为用户Id为1的用户增加"系统管理权限"角色
    u = User.query.get(1)
    admin_role = Role.query.filter(Role.name.__eq__('系统管理员')).one()
    print(u.nick_name, admin_role.name)
    # db.session.commit()
    # 将角色对象添加给用户
    u.roles.append(admin_role)
    db.session.commit()
    print('ok')


if __name__ == '__main__':
    app.app_context().push()
    db.init_app(app)
    # add_role()
    add_user_role()
    # add_user()

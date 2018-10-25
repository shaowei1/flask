'''
1. 使用Flask实现web程序，功能如下：
    • 1）配置使用mysql数据库
2）创建角色模型类和用户模型类并生成数据表
3）在视图中使用模板文件显示角色信息以及和角色关联的用户信息
    • 涉及知识点:
    • 1）Flask-SQLALCHMEY扩展的使用及配置
2）Flask中模型类的定义和数据表的创建
3）数据库的查询和关联属性的使用
'''

from flask import Flask, render_template
# 导入flask_sqlchemy扩展
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    '''setting class'''

    DEBUG = True

    # 设置数据库的链接地址
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://demouser:demopassword@localhost/admin_user'
    # 关闭追踪数据库的修改
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 配置展示SQL语句
    # app.config['SQLALCHEMY_ECHO'] = True


# 加载配置
app.config.from_object(Config)

# 需求：实现一对多的模型类定义，角色(管理员和普通用户)和用户，Role(一方)和User(多方)
#  创建一个SQLAlchemy类的对象
db = SQLAlchemy(app)


# 定义模型类
# 一对多: 角色表和用户表
class Role(db.Model):  # 管理员和普通用户
    """角色模型类"""
    # 如果不定义，会默认创建同类名的表名，it_roles/tb_roles
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True, nullable=False)
    # 关系属性: 给role对象增加一个属性users, 通过role.users可以直接获取和role关联的用户的信息
    # # backref='role'代表给User类的对象增加一个属性role，通过user.role可以直接获取和user关联的角色的信息
    # 一方定义关系
    # 第一个参数表示多方的类名，第二个参数表示反向引用，
    users = db.relationship('User', backref='role')  # 一方找多方使用role.users # 多方找一方user.role

    # 将对象显示为一个可视化字符串
    def __repr__(self):
        return 'Role: %s %s' % (self.id, self.name)


# users: 用户表
class User(db.Model):
    """用户模型类"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, index=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(64))
    # db.ForeignKey('roles.id')说明这一列一个外键列，对应roles表的id
    # 定义外键,指向一方的主键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User: %s %s %s %s %s' % (self.id, self.name, self.email, self.password, self.role_id)


def add_test_data():
    """添加测试数据"""
    # 添加角色数据
    # 实例化类对象
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()  # 提交数据到数据库中

    ro2 = Role(name='staff')
    # session数据库会话对象，add_all/add添加数据给数据库会话对象, iterable/object
    db.session.add(ro2)
    db.session.commit()  # 提交数据到数据库中

    # 添加用户数据
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()


@app.route('/roles')
def get_users_info():
    roles = Role.query.all()
    print(roles)

    return render_template('roles.html', roles=roles)


if __name__ == '__main__':
    # 先删除旧表
    db.drop_all()
    # 创建数据库表
    db.create_all()
    # # 添加测试数据
    add_test_data()
    # http://127.0.0.1:5000/roles
    app.run(debug=True)

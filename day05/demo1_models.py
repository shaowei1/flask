from flask import Flask
# 导入flask_sqlchemy扩展
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://demouser:demopassword@localhost/admin_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 配置展示SQL语句
# app.config['SQLALCHEMY_ECHO'] = True


# 需求：实现一对多的模型类定义，角色(管理员和普通用户)和用户，Role(一方)和User(多方)
# 实例化sqlalchemy对象
db = SQLAlchemy(app)


# 定义模型类
class Role(db.Model):  # 管理员和普通用户
    # 如果不定义，会默认创建同类名的表名，it_roles/tb_roles
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 一方定义关系
    # 第一个参数表示多方的类名，第二个参数表示反向引用，
    # 等号左边给一方使用，实现一对多的查询
    # 等号右边backref给多方使用，实现多对一的查询
    us = db.relationship('User', backref='role')  # user.role

    # repr方法：可以返回对象的可读字符串
    def __repr__(self):
        return 'name:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(32))
    # 定义外键,指向一方的主键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'name:%s' % self.name


"""
test use terminal
# python3
>>> from demo1_models import *
>>> User.query.filter().all()

过滤查询：
User.query.filter().all() 查询所有数据
User.query.filter(User.name=='wang').all() 查询name等于wang的数据,filter查询接收的参数，必须使用模型类的类名，可以使用运算符，必须使用查询执行器
User.query.filter_by(name='wang').all() filter_by接收的参数，只需要字段名，只能使用赋值查询，必须使用查询执行器。

分页查询：
第一个参数表示页数，第二个参数表示每页条目数，第三个False表示分页异常不报错。
paginate = User.query.filter().paginate(1,1,False) 返回的是分页对象
paginate.page 当前页数
paginate.pages 总页数
paginate.items 数据

排序查询：
User.query.order_by(User.id.desc()).all() 降序排序
User.query.order_by(User.id.asc()).all() 升序排序

限制查询结果数量：
User.query.filter().limit(2).all() 返回2条

查询结果计数：
User.query.filter().count() 

修改数据：
User.query.filter(User.name=='zhang').update({'name':'liu'})
通过查询到的对象修改数据
>>> user = User.query.filter(User.name=='zhang').first()
>>> user.name='li'
>>> db.session.add(user)
>>> db.session.commit()

关系的定义：
us = db.relationship('User',backref='role')

一对多的查询：查询管理员有多少人
role = Role.query.first()
role.us
多对一的查询：查询chen是管理员还是普通用户
user = User.query.filter(User.name=='chen').first()
user.role


"""

if __name__ == '__main__':
    # 先删除旧表
    db.drop_all()
    # 创建数据库表
    db.create_all()
    # 实例化类对象
    ro1 = Role(name='admin')
    ro2 = Role(name='user')
    # session数据库会话对象，add_all/add添加数据给数据库会话对象
    db.session.add_all([ro1, ro2])
    db.session.commit()  # 提交数据到数据库中
    us1 = User(name='wang', email='wang@163.com', pswd='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', pswd='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', pswd='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', pswd='456789', role_id=ro1.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    app.run(debug=True)

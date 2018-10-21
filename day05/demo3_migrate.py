from flask import Flask
# 导入flask_sqlchemy扩展
from flask_sqlalchemy import SQLAlchemy
# 导入管理器
from flask_script import Manager
# 导入迁移框架
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
# 配置数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://demouser:demopassword@localhost/admin_user'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 实例化管理器对象
manage = Manager(app)

# 使用迁移框架
Migrate(app, db)

# 添加迁移命令给管理器
manage.add_command('db', MigrateCommand)


# 定义模型类
class Role(db.Model):  # 管理员和普通用户
    # 如果不定义，会默认创建同类名的表名，it_roles/tb_roles
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    us = db.relationship('User', backref='role')  # user.role

    # repr方法：可以返回对象的可读字符串
    def __repr__(self):
        return 'name:%s' % self.name


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    # email = db.Column(db.String(32),unique=True)
    # 添加字段
    email = db.Column(db.String(32))
    pswd = db.Column(db.String(32))
    # 定义外键,指向一方的主键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'name:%s' % self.name


if __name__ == '__main__':
    manage.run()

'''
pip install flask-migrate

python demo3_migrate.py db init

python demo3_migrate.py db migrate -m 'initial migration'

python demo3_migrate.py db upgrade

python demo3_migrate.py db migrate -m 'mobile to email'

python demo3_migrate.py db upgrade

不建议使用history 和 downgrade 因为表结构复杂，回退不了还会产生错误，直接upgrade,或者人工比对
python demo3_migrate.py db history

python demo3_migrate.py db downgrade b8d4fba2d7d2
'''

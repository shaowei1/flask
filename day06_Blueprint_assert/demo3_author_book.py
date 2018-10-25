from flask import Flask, render_template, redirect, url_for
# 导入flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# 导入flask_wtf
from flask_wtf import FlaskForm
# 导入字段类型
from wtforms import StringField, SubmitField
# 导入验证函数
from wtforms.validators import DataRequired

app = Flask(__name__)
# 配置数据库的连接和动态追踪修改
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://demouser:demopassword@localhost/library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 设置密钥
app.config['SECRET_KEY'] = 'g+Dd+4gwlGafbwx2nOOic/tiRnn7op7nOnsUrKUNsrC38kERjK5Esg=='
# 在请求过程中自动提交数据，不用手动commit
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


"""

需求：实现作者图书案例，实现数据的增删改查

思路分析：
1、添加数据：表单、wtf扩展，开启csrf保护，设置密钥、表单域中设置csrf_token,自定义表单类，实例化表单对象，传给模板。
2、数据展示：
    2.1、模板：render_template，使用模板语法，来获取数据库中的查询结果；
    2.2、模型类：定义两个模型类，作者和图书，配置数据库的链接、动态追踪修改，创建表，添加测试数据；
3、删除数据：a标签，模板中需要传入删除数据的id值，args、form，<转换器>

实现：实现简单功能，进行版本迭代；

"""

# 实例化处理器对象
db = SQLAlchemy(app)


# 定义模型类: 作者和书籍
class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)  # 如果不指定主键，不能创建表
    name = db.Column(db.String(32), unique=True)

    def __repr__(self):
        return 'author: %s' % self.name


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)  # 如果不指定主键，不能创建表
    info = db.Column(db.String(32))
    lead = db.Column(db.String(32))

    def __repr__(self):
        return 'book: %s' % self.info


# 自定义表单类
class Form(FlaskForm):
    wtf_author = StringField(validators=[DataRequired()])
    wtf_book = StringField(validators=[DataRequired()])
    wtf_submit = SubmitField('save')


# 主要业务逻辑：展示数据
@app.route('/', methods=['GET', 'POST'])
def index():
    # 实例化表单对象
    form = Form()
    authors, books = None, None
    # 进行异常处理,数据库的增删改查
    try:
        # 查询作者和书籍
        authors = Author.query.all()
        books = Book.query.all()
    except Exception as e:
        print(e)
    # 如果是post请求，获取作者和书籍的参数
    if form.validate_on_submit():
        # 使用表单对象获取数据
        wtf_auth = form.wtf_author.data
        wtf_book = form.wtf_book.data
        # 必须构建模型类对象
        au = Author(name=wtf_auth)
        bk = Book(info=wtf_book)
        # 错误：直接把参数提交到数据库，把数据存入数据
        # db.session.add_all([wtf_auth,wtf_book])
        # 添加模型类的对象
        try:
            db.session.add_all([au, bk])
            db.session.commit()
        except Exception as e:
            print(e)
            # 提交数据如果不成功，需要进行回滚
            db.session.rollback()
        # 提交数据后，需要再次查询
        try:
            # 查询作者和书籍
            authors = Author.query.all()
            books = Book.query.all()
        except Exception as e:
            print(e)

    return render_template('demo2_author_book.html', authors=authors, books=books, form=form)


# 定义删除作者的视图函数
@app.route("/delete_author/<int:id>")
def del_author(id):
    # 根据id查询数据库
    # auth = Author.query.filter(Author.id==id).first()
    # auth = Book.query.fitler_by(id=id).first()    # 等值过滤器
    auth = None
    try:
        auth = Author.query.get(id)
    except Exception as e:
        print(e)

    try:
        db.session.delete(auth)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    # 删除后需要动态展示删除后的数据，需要再次查询
    # 因为index视图函数中已经实现查询，所以使用反向解析，直接定位到index视图函数，不需要再次查询
    return redirect(url_for('index'))


# 删除书籍
@app.route('/delete_book<int:id>')
def del_book(id):
    book = Book.query.filter(Book.id == id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.drop_all()
    db.create_all()
    # test_data
    au_xi = Author(name='我吃西红柿')
    au_qian = Author(name='萧潜')
    au_san = Author(name='唐家三少')
    bk_xi = Book(info='吞噬星空')
    bk_xi2 = Book(info='寸芒')
    bk_qian = Book(info='飘渺之旅')
    bk_san = Book(info='斗罗大陆')
    # 把数据提交给用户会话
    db.session.add_all([au_xi, au_qian, au_san, bk_qian, bk_san, bk_xi, bk_xi2])
    # commit 会话
    db.session.commit()

    app.run(debug=True)

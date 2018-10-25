import unittest
# 导入测试代码
from demo3_author_book import *


# 单元测试：
# 自定义测试类，必须继承自TestCase
class DatabaseTest(unittest.TestCase):

    # 函数名固定，首先被执行，一般用来初始化操作
    def setUp(self):
        self.app = app
        # 开启测试标记，帮助定位测试的错误, 是Flask提供的assert
        # app.config['TESTING'] = True
        # 指定链接的数据库
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://demouser:demopassword@localhost/library'
        db.create_all()

    # 函数名固定，最后被执行，一般用来扫尾工作
    def tearDown(self):
        # 移除数据库会话对象
        db.session.remove()
        db.drop_all()

    # 测试方法，函数名必须以test开头,模拟添加数据
    def test_add_data(self):
        shaowei = Author(name='shaowei')
        book = Book(info='python')
        db.session.add_all([shaowei, book])
        db.session.commit()
        # 查询数据库
        auth = Author.query.filter(Author.name == 'shaowei').first()
        # author: shaowei book: python
        # <class 'demo3_author_book.Author'>
        # auth 是一个class对象，可以点击filter第一个查看
        bk = Book.query.filter_by(info='python').first()
        # 断言数据一定存在
        print(auth, bk)
        print(type(auth))
        # self.assertIsNotNone(auth)
        # self.assertIsNotNone(bk)

        # 断言相等
        self.assertEqual(auth.name, 'shaowei')

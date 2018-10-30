from flask import Blueprint
# 创建蓝图对象
news_blue = Blueprint('news_blue',__name__)

# 把使用蓝图对象的文件导入到创建蓝图对象的👇
from . import views


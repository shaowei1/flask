from flask import Blueprint

# create a blueprint object
admin = Blueprint('admin', __name__)
from demo2_admin_new import new


@admin.route('/')
def admin_home():
    """后台主页"""
    return 'admin_home'


@admin.route('/edit')
def edit():
    """编辑"""
    return 'edit'


@admin.route('/publish')
def publish():
    """发布博客"""
    return 'publish'

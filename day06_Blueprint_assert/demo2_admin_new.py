from demo2_admin import admin


@admin.route('/new')
def new():
    """创建"""
    return 'new'

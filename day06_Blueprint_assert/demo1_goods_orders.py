from demo1_temp_file import api


@api.route('/goods')
def goods():
    return 'goodes'


@api.route('/orders')
def orders():
    return 'orders'

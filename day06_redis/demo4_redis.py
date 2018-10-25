from redis import StrictRedis


# 实例化连接redis数据库的对象
# decode_response表示解码响应，默认为False，取出数据为bytes类型，
cli = StrictRedis(decode_responses=True)

# 设置数据
cli.set('hello','world')

# 获取数据
print(cli.get('hello'))



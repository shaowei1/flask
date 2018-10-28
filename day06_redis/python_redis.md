## install

安装Redis的有3种方式https://github.com/andymccurdy/redis-py

第一种：进⼊虚拟环境py_django，联⽹安装包redis
pip install redis

第二种：进⼊虚拟环境py_django，联⽹安装包redis
easy_install redis

第三种：到中⽂官⽹-客户端下载redis包的源码，使⽤源码安装
一步步执行 wget https://github.com/andymccurdy/redis-py/archive/master.zip
unzip master.zip
cd redis-py-master
sudo python setup.py install

## 调⽤模块
引⼊模块
from redis import *
redis.py模块封装了redis配置信息和基本操作

redis.py提供了两个类用于和redis 数据库交互,StrictRedis用于实现官方的语法和命令，　Redis是StrictRedis的子类,用于向后兼容老版本
这个模块中提供了StrictRedis对象(Strict严格)，⽤于连接redis服务器，并按照不同类型提供 了不同⽅法，进⾏交互操作

## StrictRedis对象⽅法
通过init创建对象，指定参数host、port与指定的服务器和端⼝连接，host默认为localhost，port默认为6379，db默认为0
sr = StrictRedis(host='localhost', port=6379, db=0)

    简写
    sr=StrictRedis()
    根据不同的类型，拥有不同的实例⽅法可以调⽤，与前⾯学的redis命令对应，⽅法需要的参数与命令的参数⼀致
    
    string
        set
        setex
        mset
        append
        get
        mget
        key
    keys
        exists
        type
        delete
        expire
        getrange
        ttl
    hash
        hset
        hmset
        hkeys
        hget
        hmget
        hvals
        hdel
    list
        lpush
        rpush
        linsert
        lrange
        lset
        lrem
    set
        sadd
        smembers
        srem
    zset
        zadd
        zrange
        zrangebyscore
        zscore
        zrem
        zremrangebyscore
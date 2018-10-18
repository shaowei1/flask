# 代码复用

## 继承block(important)
顶部底部中间部分内容
模板不支持多重继承
endblock(结束标签可以起名字)结束离它最近的

## 宏Macro(相当于function)　only use in template
作用: 模板复用
根据参数不同封装动态代码块

### difference
继承: 固定一样的<br>
宏: 可调用, 可传参, 可封装，(起别名: 防止调用重名)

## 包含(include)
copy完全复制
ignore missing

# 特有变量／函数（特殊: 既可以在视图，也可以在模板中用)
config


request
{{request.url}}

session

g (临时存储数据)

url_for()

get_flashed_messages()(消息闪现)
提示用户信息(有可能会报错,不建议使用, ascii错误, 浏览器重启能解决)
u''也不能解决
flash('') # 列表容器


# web表单(flask-wtf)
表单: 刷新页面会自动提交数据

demo3 - debug

模板加载不需要使用action

urandom
base64

前端／后端校验
postman
spider
程序


hacker怎么知道你刚访问了哪个网站
cookies同源策略,
把正常网站有安全漏洞url放入到自己的网站中，对外隐藏参数(<a><img>)
钓鱼网站

保护


环境变量

一对多
多对多

自关联一对多
省   市　  区
朋友圈     你也用我也用

自关联多对多
微博      粉　   被粉


列　原子性   不可分割
表当中必须要有主键依赖
非主属性之间不存在依赖关系...   

## sql
oracle  几百万

ORM --> sql语句


## 蓝图
实现多个文件路由映射
script_flask config 可以配置port




# 任务
转图片格式jpg    格式转换　   240像素       自动传参数
环境  语言
多进程，多线程，协程
数据量     性能优化
异常处理


TRACK   内存



100 200 row code

9:30    12:30
50张列表

flask_mysql 看视频

1-多 backref
primmary join   多多

重写套钱



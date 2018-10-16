# 基本程序的扩展
1. 返回状态码和abort函数

2. 重定向

3. JSON

4. 给URL传递参数<>

5. 正则URL

6. 状态保持

    因为 http 是一种无状态协议，浏览器请求服务器是无状态的。
    
    无状态：指一次用户请求时，浏览器、服务器无法知道之前这个用户做过什么，每次请求都是一次新的请求。
    
    无状态原因：浏览器与服务器是使用 socket 套接字进行通信的，服务器将请求结果返回给浏览器之后，会关闭当前的 socket 连接，而且服务器也会在处理页面完毕之后销毁页面对象。
    有时需要保持下来用户浏览的状态，比如用户是否登录过，浏览过哪些商品等
    
    实现状态保持主要有两种方式：
    在客户端存储信息使用Cookie
    在服务器端存储信息使用Session<br>
    
    无状态协议:<br>
    协议对于事务处理没有记忆能力<br>
    对同一个 url 请求没有上下文关系<br>
    每次的请求都是独立的，它的执行情况和结果与前面的请求和之后的请求是无直接关系的，它不会受前面的请求应答情况直接影响，也不会直接影响后面的请求应答情况<br>
    服务器中没有保存客户端的状态，客户端必须每次带上自己的状态去请求服务器<br>
    人生若只如初见

7. 请求勾子

    为了让每个视图函数避免编写重复功能的代码，Flask提供了通用设施的功能，即请求钩子。
    
    在客户端和服务器交互的过程中，有些准备工作或扫尾工作需要处理，比如：
    
    在请求开始时，建立数据库连接；<br>
    在请求开始时，根据需求进行权限校验；<br>
    在请求结束时，指定数据的交互格式；

8. 程序加载配置

    在 Flask 程序运行的时候，可以给 Flask 设置相关配置，比如：配置 Debug 模式，配置数据库连接地址等等，设置 Flask 配置有以下三种方式：
    从配置对象中加载(常用)
    
    app.config.from_object()
    
    从配置文件中加载
    
    app.config.from_pyfile()
    
    从环境变量中加载(了解)
    
    app.config.from_envvar()
    
# 上下文
客户端发送请求，服务器回复响应。

上下文（RequestContext）：

1、request封装了HTTP请求作为对象。

2、session封装了用户信息作为对象

# request
request 就是flask中代表当前请求的 request 对象，其中一个请求上下文变量(理解成全局变量，在视图函数中直接使用可以取到当前本次请求)

常用的属性如下：

|属性|	说明	|类型|<br>
|---|---|----|---|
data	|记录请求的数据，并转换为字符串|	*<br>
form	|记录请求中的表单数据	|MultiDict<br>
args	|记录请求中的查询参数	|MultiDict<br>
cookies	|记录请求中的cookie信息|	Dict<br>
headers	|记录请求中的报文头	|EnvironHeaders<br>
method|	记录请求使用的HTTP方法	|GET/POST<br>
url|	记录请求的URL地址	|string<br>
files|	记录请求上传的文件	|*<br>

# Decorator Route
![](./flask_route.png)

Flask有两大核心：Werkzeug和Jinja2

- Werkzeug实现路由、调试和Web服务器网关接口
- Jinja2实现了模板。

Werkzeug是一个遵循WSGI协议的python函数库

- 其内部实现了很多Web框架底层的东西，比如request和response对象；
- 与WSGI规范的兼容；支持Unicode；
- 支持基本的会话管理和签名Cookie；
- 集成URL请求路由等。

Werkzeug库的 routing 模块负责实现 URL 解析。不同的 URL 对应不同的视图函数，routing模块会对请求信息的URL进行解析，匹配到URL对应的视图函数，执行该函数以此生成一个响应信息。

routing模块内部有：

Rule类
<br>用来构造不同的URL模式的对象，路由URL规则

Map类<br>
存储所有的URL规则和一些配置参数

BaseConverter的子类
<br>负责定义匹配规则

MapAdapter类<br>
负责协调Rule做具体的匹配的工作


# 杂记
类名() # 会执行类

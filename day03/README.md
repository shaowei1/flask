## 视图和路由
1. decorate router
![](../day02/flask_route.png)

### global
每个人的请求是没有关系的,就算你们请求相同的东西, 假设40个线程,40个request,请求结束(response),销毁request,(线程内的全局变量)

## flask_script 
使用flask_script 一部分好处
可以在终端自定义host, port, debug, 
相似sys, argv
一个服务器有多个ip,方便设置

## 模板
业务处理
返回数据
浏览器可以接收数据，渲染，为什么要用template

(解耦，耦合度降低)  渲染数据

模板引擎

## 过滤器(only use in template)
reverse<br>
一般实现first 和 last 交换<br>

safe , 让模板按照超文本语言的语意解析数据<br>
模板默认开启转译, js会操作数据很可怕

html　渲染数据
css     渲染样式
js      动态效果，　操作dom树, 数据交互 


<>里面是对象

f.__name__函数名

## template extend
```html
<h1>page info<h1>   # 卸载extends能识别，但不推荐使用，　一个html中代码太多(taobao 几千行），extends写在第一行
从extends之下，相当于都是继承父模板
只能在block中使用

继承的本质: 代码替换
base 共有的内容
特有的block

```

# Flask框架第三天
## 视图
### 装饰器路由的实现原理
* Rule
    * 存储具体的url和视图函数名的映射关系，包含请求方法
* Map
    * 存储多个Rule类对象，Map是列表容器
        * 为什么是列表容器？？？
* MapAdapter
    * 匹配具体的url和视图
### 上下文对象
* 请求上下文
    * request
        * 获取http请求的数据，常用属性：args/form/files/cookies/method/url/headers/
    * session
        * 实现状态保持，设置session信息
* 应用上下文
    * current_app
        * 程序运行过程中存储的配置信息，用来记录项目日志
    * g
        * 用来临时存储数据，用来记录用户身份
### flask_script扩展包
* 实例化管理器对象,和程序实例关联，代替app调用run方法，必须使用脚本参数runserver
* 在终端可以手动运行代码，传入主机和端口
    * 可以配合flask_migrate扩展实现数据库的迁移
## 模板
### 概念
* 包含响应文本的文件，不是特指html格式文件
### 作用
* 接收视图返回的数据，渲染数据，程序解耦
### 语法
* {{ 变量 }}
* 语句：{% if 表达式 %} {% endif %}
* loop.index从第一个遍历，loop.index0从第0个遍历
### 继承
* 共有的内容留下，特有的内容定义block，让子类实现
* 灵活运用

![](/templates/Flask框架第三天.png)
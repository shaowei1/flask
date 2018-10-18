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




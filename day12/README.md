## project
属于　单进程，单线程

scrapy本身支持
scrapy 核心是单线程，但是利用twisted支持多线程

如果多个人访问，  多个request对象，多个线程，互不干扰

上下文对象
请求过程中存在,结束就自动销毁

    request, session, current_app, g : 4个都是在一个线程中的
    
    请求上下文对象
    request
    session
    
    应用上下文对象
    current_app
    g
    
## iframe
iframe  方便，点击，不需要各种数据交互    
        对爬虫不友好，不好定位，
        
```html
<!DOCTYPE html>
<html>
<body>

<iframe src="https://www.w3schools.com">
  <p>Your browser does not support iframes.</p>
</iframe>

</body>
</html>

```        
target  子页面:url

url_for     endpoint

## 前后端分离的一种设计风格        
restful       风格

http

    get
    post
    put
    delete

## 制作外国网站时，需求不同
facebook    50多个性别


## 缓存，
redis缓存中和硬盘中的不一样怎么办?
有效期之内缓存和硬盘不一样

缓存和磁盘的关系
    缓存快
    一个小时mysql改变
    缓存－－－磁盘－－－缓存(先在缓存(redis)中找，找不到人后去磁盘(mysql)中,然后存储在缓存中，返回界面)
    
    # problem
    
        硬盘中修改了，但是缓存中并没有刷新
        
    # solution
    
        手动清除cache
    

## IO
网络io

磁盘io

## 网盘的秒传
秒传

md5(哈希计算)　= 数据       (跟文件名没有关系，文件内部的二进制，经过md5加密，会有一个标志，能给视频文件去重, 给文件一个引用)

## 网速
1.25    1/8

2020  -->  ５G

## picture save
矢量图 : 能达到700M

没有第三方存储怎么办:
    fastDFS 存图片
    
用户头像一般存相对路径

新闻图片存绝对路径，因为图片对于新闻比较重要，图片挂了新闻也可以挂了    

头像圆形: 全屏，剪切 --> 前端效果

直接就可以看到图片路径，不好

## 一般传密码之类的信息
前端加密    -->      传输数据   --> server


##七牛云
   上海公司  华北
    
    通过q　权重
    token   令牌
    上传文件到仓库



## 
默认模板界面，没有接口

接口参数比较多的: 租房信息几十个参数


## 一种新的提交博客方式
资源，retext

附文本编辑器(在html中)，前端插件

## 怎么检测的
检测到立马就显示


## ajaxsubmit

```python
'''
ajaxForm()和ajaxSubmit()的可选参数项对象

 ajaxForm 和 ajaxSubmit 都支持大量的可选参数，它们通过可选参数项对象传入。可选参数项对象只是一个简单的 JavaScript对象，里边包含了一些属性和一些值:


target

用server端返回的内容更换指定的页面元素的内容。 这个值可以用jQuery 选择器来表示, 或者是一个jQuery 对象， 一个 DOM 元素。
缺省值： null


url

表单提交的地址。
缺省值： 表单的action的值


type

表单提交的方式，'GET' 或 'POST'.
缺省值： 表单的 method 的值 (如果没有指明则认为是 'GET')


beforeSubmit

表单提交前执行的方法。这个可以用在表单提交前的预处理，或表单校验。如果'beforeSubmit'指定的函数返回false，则表单不会被提交。 'beforeSubmit'函数调用时需要3个参数：数组形式的表单数据，jQuery 对象形式的表单对象，可选的用来传递给ajaxForm/ajaxSubmit 的对象。

数组形式的表单数据是下面这样的格式：[ { name: 'username', value: 'jresig' }, { name: 'password', value: 'secret' } ]

缺省值： null


success

当表单提交后执行的函数。 如果'success' 回调函数被指定，当server端返回对表单提交的响应后，这个方法就会被执行。 responseText 和 responseXML 的值会被传进这个参数 (这个要依赖于dataType的类型).
缺省值： null

 

dataType

指定服务器响应返回的数据类型。其中之一: null, 'xml', 'script', 或者 'json'. 这个 dataType 选项用来指示你如何去处理server端返回的数据。 这个和 jQuery.httpData 方法直接相对应。

下面就是可以用的选项：

'xml': 如果 dataType == 'xml' 则 server 端返回的数据被当作是 XML 来处理， 这种情况下'success'指定的回调函数会被传进去 responseXML 数据

'json': 如果 dataType == 'json' 则server端返回的数据将会被执行，并传进'success'回调函数

'script': 如果 dataType == 'script' 则server端返回的数据将会在上下文的环境中被执行

缺省值： null


semantic

一个布尔值，用来指示表单里提交的数据的顺序是否需要严格按照语义的顺序。一般表单的数据都是按语义顺序序列化的，除非表单里有一个type="image"元素. 所以只有当表单里必须要求有严格顺序并且表单里有type="image"时才需要指定这个。
缺省值： false


resetForm

布尔值，指示表单提交成功后是否需要重置。
缺省值： null

 

clearForm

布尔值，指示表单提交成功后是否需要清空。
缺省值： null


iframe

布尔值，用来指示表单是否需要提交到一个iframe里。 这个用在表单里有file域要上传文件时。更多信息请参考 代码示例 页面里的File Uploads 文档。 
缺省值： false


'''
```


jinjia2 继承extend详细了解

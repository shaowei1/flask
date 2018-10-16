from flask import Flask

app = Flask(__name__)

"""
var params = {
    'name':zhangsan,
    'age':18
}

$.ajax({
    url:'/',
    type:'get',
    data:JSON.stringify(params),# 把对象转成json字符串
    contentType:'application/json',# 发送到后端的数据格式
    dataType:'json'# 获取后端返回的数据格式为json
    success:function(resp){
        if (resp == 666){
            alert(信息)
        }elif(resp == 'hello world'){
            alert(信息)
        } 
    }
})

errno = 666
errmsg = '用户名已注册'
# 通过判断数字(errno) 给用户显示信息(errmsg), 前后端数据交互
"""


# 状态码：标识http请求信息的编码。
# return 可以返回不符合http协议的状态码，
# 作用：自定义的状态码，用来实现前后端的数据交互
@app.route('/')
def index():
    return 'hello world'
    # HTTP/1.0 200 OK
    # return 'hello world', 404
    # HTTP/1.0 404 NOT FOUND
    # return 'hello world', 666
    # HTTP/1.0 666 UNKNOWN


if __name__ == '__main__':
    app.run(debug=True)

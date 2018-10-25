from flask import Flask, render_template, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'python33'


# 宏的使用：
@app.route('/')
def index():
    flash('请输入用户名信息')
    return render_template('demo1_macro.html')
    # return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=8888)

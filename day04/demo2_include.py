from flask import Flask, render_template

app = Flask(__name__)


# 包含的使用：
@app.route('/')
def index():
    return render_template('demo2_include.html')


if __name__ == '__main__':
    app.run(debug=True)

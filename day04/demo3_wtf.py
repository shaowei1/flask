from flask import Flask, render_template
# 导入wtf扩展提供的表单类
from flask_wtf import FlaskForm  # Form 已经不建议使用，现在使用FlaskForm
# 导入wtf扩展提供的字段类型
from wtforms import StringField, PasswordField, SubmitField
# 导入wtf扩展提供的验证函数
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
# 设置密钥
app.config['SECRET_KEY'] = 'IcZrYb7U2c2Q56h3xF+PAnxj1sHBVYLp6fErP805kHrMRcccAtMuig=='


# 自定义表单类
class Form(FlaskForm):
    user = StringField(validators=[DataRequired()])
    pswd = PasswordField(validators=[DataRequired(), EqualTo('pswd2')])
    pswd2 = PasswordField(validators=[DataRequired()])
    submit = SubmitField('注册')


# 需求：通过wtf扩展实现注册表单，用户名、密码、确认密码、提交按钮，并且获取表单数据
@app.route('/', methods=['GET', 'POST'])
def index():
    # 实例化表单对象
    form = Form()
    print(form.validate_on_submit())
    # 使用表单提供的函数，验证表单数据是否符合条件
    # 不仅会调用验证器，验证数据是否符合条件
    # 还会验证表单中是否设置csrf_token
    # 条件都满足，返回值True，否则False
    if form.validate_on_submit():
        # 获取表单数据，模拟注册
        us = form.user.data
        ps = form.pswd.data
        ps2 = form.pswd2.data
        print(us, ps, ps2)
        print(form.validate_on_submit())

    return render_template('demo3_wtf.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

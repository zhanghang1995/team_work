#coding:utf8

from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from app.models import Test

class LoginForm(FlaskForm):
    #<input type="text" class="form-control" id="inputEmail3" placeholder="用户名或电子邮件">
    #管理员登陆表单
    username = StringField(
        label="账号",
        validators = [
            DataRequired("请用户名或电子邮件！")
        ],
        description="账号",
        render_kw = {
            "placeholder":"请用户名或电子邮件！",
            "class":"form-control",
            # "required":"required"
        }
    )
    #<input type="password" class="form-control" id="inputPassword3" placeholder="密　码">
    password = PasswordField(
        label="密码",
        validators=[
          DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "class":"form-control",
            "placeholder": "请输入密码！"
            # "required": "required"
        }
    )

    submit = SubmitField(
        label='登录',
        render_kw={
            "class":"btn btn-default"
        }
    )

    # def validate_account(self, field):
    #     account = field.data
    #     admin = Test.query.filter_by(username=account).count()
    #     if admin == 0:
    #         return render_template("admin/erro.html")
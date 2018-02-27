#coding:utf8

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,ValidationError
from app.models import Test

class LoginForm(FlaskForm):
    #管理员登陆表单
    account = StringField(
        label="账号",
        validators = [
            DataRequired("请输入账号！")
        ],
        description="账号",
        render_kw = {
            "placeholder":"请输入账号！",
            # "required":"required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
          DataRequired("请输入密码！")
        ],
        description="密码",
        render_kw={
            "placeholder": "请输入密码！",
            # "required": "required"
        }
    )

    submit = SubmitField(
        '登录',
    )

    def validate_account(self, field):
        account = field.data
        admin = Test.query.filter_by(username=account).count()
        if admin == 0:
            raise ValidationError("账号不存在! ")
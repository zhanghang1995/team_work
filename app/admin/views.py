#
#蓝图：一个应用中或跨应用制作应用组件和支持通用的模式
from .import admin
from flask import render_template
from app.admin.forms import LoginForm
@admin.route("/")
def index():
    return "<h1 style='color:red'>this is admin</h1>"

@admin.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data()
    return render_template("admin/login.html",form=form)


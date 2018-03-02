#
#蓝图：一个应用中或跨应用制作应用组件和支持通用的模式
from .import home
from flask import render_template,redirect,url_for

@home.route("/")
def index():
    return render_template("admin/main/test.html")

@home.route("/login/")
def login():
    return render_template("home/login.html")

@home.route("/logout/")
def logout():
    return redirect(url_for("home.login"))

@home.route("/register/")
def register():
    return render_template("home/register.html")


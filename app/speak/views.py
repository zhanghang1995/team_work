#coding:utf-8
#此处定义后台语音处理模块

from . import speak
from flask import url_for,request,render_template

@speak.route("/",methods=["GET", "POST"])
def index():
    return render_template("speak/speak.html", )

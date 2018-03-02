#
#蓝图：一个应用中或跨应用制作应用组件和支持通用的模式
from .import admin
from flask import render_template,redirect,flash,url_for,session,request
from app.admin.forms import LoginForm
from app.models import Test
@admin.route("/",methods=["GET", "POST"])
def index():
    return render_template("admin/main.html", )


@admin.route("/login/", methods=["GET", "POST"])
def login():
    """
    后台登录
    """
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Test.query.filter_by(username=data["username"]).first()
        # 密码错误时，check_pwd返回false,则此时not check_pwd(data["pwd"])为真。
        if admin is None or admin.password != data["password"]:
            flash("用户名或密码错误!")
            return redirect(url_for("admin.login"))
        # 如果是正确的，就要定义session的会话进行保存。
        session["admin"] = data["username"]
        return redirect(url_for('admin.index'))
    return render_template("admin/login.html", form=form)

@admin.route('/skill')
def menu():
    return render_template('admin/main/skill.html')

@admin.route('/menu')
def menu():
    return render_template('admin/main/test.html')

@admin.route('/operation')
def operation():
    return render_template('admin/main/operation.html')

@admin.route('/resource')
def menu():
    return render_template('admin/main/resource.html')

@admin.route('/loader')
def menu():
    return render_template('admin/main/loader.html')


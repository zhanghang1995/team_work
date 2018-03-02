#创建app对象
from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template
import pymysql
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:950929@localhost:3309/test"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True
app.config["SECRET_KEY"] = "7280af24be5d46fea1d15a0904da438f"
app.debug = True
db = SQLAlchemy(app)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint
from app.speak import speak as speak_blueprint


app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint,url_prefix='/admin')
app.register_blueprint(speak_blueprint,url_prefix='/speak')

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"),404

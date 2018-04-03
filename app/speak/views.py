#coding:utf-8
#此处定义后台语音处理模块

from . import speak
from flask import url_for,request,render_template,Response
import json
from app.utils.wordTag import possegation
from app.service.searchWeather import seweather
from app.utils.time import get_time
from app.utils.constant import DINNER_TIME1,DINNER_TIME2

@speak.route("/",methods=["GET", "POST"])
def index():
    return render_template("speak/speak.html", )

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@speak.route("/deal",methods=["POST"])
def speak():
    # list_data = []
    # if request.method == 'POST'and request.form.get('userwords'):
    #     # POST:
    #     # request.form获得所有post参数放在一个类似dict类中,to_dict()是字典化
    #     # 单个参数可以通过request.form.to_dict().get("xxx","")获得
    #     # ----------------------------------------------------
    #     # GET:
    #     # request.args获得所有get参数放在一个类似dict类中,to_dict()是字典化
    #     # 单个参数可以通过request.args.to_dict().get('xxx',"")获得
    #     # datax = request.form.to_dict()
    #     # content = str(datax)
    #     # resp = Response_headers(content)
    #     # return resp
    #     #此处获取用户返回的语音信息
    #     data = request.form.to_dict()
    #     if data['type'] == '0':
    #         if data['userwords'] == '好的':
    #             if get_time() > DINNER_TIME1 and get_time() < DINNER_TIME2:
    #                 content = str("晚饭想吃什么呢？")
    #                 resp = Response_headers(content)
    #                 return resp
    #             else:
    #                 content = str("晚饭想吃什么呢？")
    #                 resp = Response_headers(content)
    #                 return resp
    #         else:
    #             content = str("你喜欢吃什么？")
    #             resp = Response_headers(content)
    #             return resp
    #     else:
    #         words = possegation(data['userwords'])
    #         '''
    #             此处获取用户的语言后进行意图的识别与判断
    #         '''
    #         for key in words:
    #             # 只先提提取出用户的名词和动词
    #             if words[key] == 'ns':
    #                 if key is not None:
    #                     list_data.append(key)
    #         result = seweather(list_data[0])
    #         content = str(result)
    #         resp = Response_headers(content)
    #         return resp
    # else:
    #     content = json.dumps({"error_code": "1001"})
    #     resp = Response_headers(content)
    #     return resp



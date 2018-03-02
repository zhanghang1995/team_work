#coding:utf-8
#此处定义后台语音处理模块

from . import speak
from flask import url_for,request

@speak.route('/speakword',method=["POST"])
def analysis_word(word):
    word = request.data['word']

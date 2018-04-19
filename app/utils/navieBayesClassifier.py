# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 16:15:04 2018
配上ML的情感分析
@author: 74993
"""
from nltk.classify import NaiveBayesClassifier
import jieba

#训练集


#好的
s1 = "好的"
s2 = "可以"
s3 = "没问题"
s4 = "快点去办"
s5 = "好"
s6 = "就这样办"

#换套餐
s7 = "不喜欢吃"
s8 = "换个套餐"
s9 = "换个试试"
s10 = "太难吃了"
s11 = "换一个"
s12 = "不好吃"

#不吃
s13 = "不想吃"
s14 = "不吃了"
s15 = "吃过了"
s16 = "早就吃了"
s17 = "心情不好不想吃"

#稍后提醒
s18 = "等会我在吃"
s19 = "等会吃"
s20 = "等会提醒我"
s21 = "现在很忙，等会提醒我"

#想吃
s22 = "我想吃什么"
s23 = "我要吃什么"
s24 = "那就吃什么"
s25 = "吃"


#起床了
s26 = "起来了"
s27 = "已经起了"
s28 = "醒了"
s29 = "不睡了"

#等会叫我起来
s30 = "再睡会儿"
s31 = "一会儿再叫我"
s32 = "想再睡会儿"
s33 = "困死了"

def pretokenize(a):
    return jieba.cut(a)

def preprocess(s):
    return {word:True for word in s}

def modeal_train():
    training_data = [[preprocess(pretokenize(s1)),'好的'],
                     [preprocess(pretokenize(s2)),'好的'],
                     [preprocess(pretokenize(s3)),'好的'],
                     [preprocess(pretokenize(s4)),'好的'],
                     [preprocess(pretokenize(s5)),'好的'],
                     [preprocess(pretokenize(s6)),'好的'],
                     [preprocess(pretokenize(s7)),'换套餐'],
                     [preprocess(pretokenize(s8)),'换套餐'],
                     [preprocess(pretokenize(s9)),'换套餐'],
                     [preprocess(pretokenize(s10)),'换套餐'],
                     [preprocess(pretokenize(s11)),'换套餐'],
                     [preprocess(pretokenize(s12)),'换套餐'],
                     [preprocess(pretokenize(s13)),'不吃'],
                     [preprocess(pretokenize(s14)),'不吃'],
                     [preprocess(pretokenize(s15)),'不吃'],
                     [preprocess(pretokenize(s16)),'不吃'],
                     [preprocess(pretokenize(s17)),'不吃'],
                     [preprocess(pretokenize(s18)),'稍后提醒'],
                     [preprocess(pretokenize(s19)),'稍后提醒'],
                     [preprocess(pretokenize(s20)),'稍后提醒'],
                     [preprocess(pretokenize(s21)),'稍后提醒'],
                     [preprocess(pretokenize(s22)), '想吃'],
                     [preprocess(pretokenize(s23)), '想吃'],
                     [preprocess(pretokenize(s24)), '想吃'],
                     [preprocess(pretokenize(s25)), '想吃'],
                     [preprocess(pretokenize(s26)), '起床了'],
                     [preprocess(pretokenize(s27)), '起床了'],
                     [preprocess(pretokenize(s28)), '起床了'],
                     [preprocess(pretokenize(s29)), '起床了'],
                     [preprocess(pretokenize(s30)), '等会叫我起来'],
                     [preprocess(pretokenize(s31)), '等会叫我起来'],
                     [preprocess(pretokenize(s32)), '等会叫我起来'],
                     [preprocess(pretokenize(s33)), '等会叫我起来']]

    model = NaiveBayesClassifier.train(training_data)
    return model



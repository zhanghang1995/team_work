# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 16:15:04 2018
配上ML的情感分析
@author: 74993
"""
from nltk.classify import NaiveBayesClassifier
import jieba

#训练集
s1 = '你吃饭了吗？'
s2 = '你吃了吗？'
s3 = '吃饭吗？'
s4 = '米饭吃了吗？'
s5 = '我要订外卖'
s6 = '订外卖'
s7 = '快给我顶个外卖'
s8 = '来一份外卖'
s9 = '我要睡觉'
s10 = '睡啦'
s11 = '我困了'
s12 = '要睡觉哦了'

def pretokenize(a):
    return jieba.cut(a)

def preprocess(s):
    return {word:True for word in s}

training_data = [[preprocess(pretokenize(s1)),'吃饭'],
                 [preprocess(pretokenize(s2)),'吃饭'],
                 [preprocess(pretokenize(s3)),'吃饭'],
                 [preprocess(pretokenize(s4)),'吃饭'],
                 [preprocess(pretokenize(s5)),'外卖'],
                 [preprocess(pretokenize(s6)),'外卖'],
                 [preprocess(pretokenize(s7)),'外卖'],
                 [preprocess(pretokenize(s8)),'外卖'],
                 [preprocess(pretokenize(s9)),'睡觉'],
                 [preprocess(pretokenize(s10)),'睡觉'],
                 [preprocess(pretokenize(s11)),'睡觉'],
                 [preprocess(pretokenize(s12)),'睡觉']]

model = NaiveBayesClassifier.train(training_data)

print(model.classify(preprocess(pretokenize('我睡觉前要吃外卖'))))


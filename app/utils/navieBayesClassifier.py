# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 16:15:04 2018
配上ML的情感分析
@author: 74993
"""
from nltk.classify import NaiveBayesClassifier
import jieba

#训练集
s1 = '早上吃什么？'
s2 = '早上怎么吃？'
s3 = '早上如何吃？'
s4 = '早上想要吃什么？'
s5 = '上喜欢吃什么？'
s6 = '中午吃什么？'
s7 = '中午怎么吃？'
s8 = '中午想要吃什么？'
s9 = '中午喜欢吃什么？'
s10 = '晚上吃什么？'
s11 = '晚上吃什么？'
s12 = '晚上怎么吃？'
s13 = '晚上想要吃什么？'
s14 = '晚上喜欢吃什么？'
s15 = '晚上吃什么？'

def pretokenize(a):
    return jieba.cut(a)

def preprocess(s):
    return {word:True for word in s}

training_data = [[preprocess(pretokenize(s1)),'问吃什么'],
                 [preprocess(pretokenize(s2)),'问吃什么'],
                 [preprocess(pretokenize(s3)),'问吃什么'],
                 [preprocess(pretokenize(s4)),'问吃什么'],
                 [preprocess(pretokenize(s5)),'问吃什么'],
                 [preprocess(pretokenize(s6)),'问吃什么'],
                 [preprocess(pretokenize(s7)),'问吃什么'],
                 [preprocess(pretokenize(s8)),'问吃什么'],
                 [preprocess(pretokenize(s9)),'问吃什么'],
                 [preprocess(pretokenize(s10)),'问吃什么'],
                 [preprocess(pretokenize(s11)),'问吃什么'],
                 [preprocess(pretokenize(s12)),'问吃什么']]

model = NaiveBayesClassifier.train(training_data)

print(model.classify(preprocess(pretokenize('我睡觉前要吃外卖'))))


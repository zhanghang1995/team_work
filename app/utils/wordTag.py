#使用jieb分词进行词性标注

import jieba.posseg as pseg
import json

def possegation(data):
    words = pseg.cut(data)
    result_data = gentodict(words)
    return result_data


#分词后词性的处理（将处理的generator 处理成为 list 再有list方式转化为 dict（））

def gentodict(data):
    list2 = []
    list1 = []
    result = {}
    for flag,word in data:
        list1.append(str(flag))
        list2.append(str(word))
        result = dict(zip(list1,list2))
    return result
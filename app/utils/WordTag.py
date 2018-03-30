#使用jieb分词进行词性标注

import jieba.posseg as pseg

def possegation(data):
    words = pseg.cut(data)
    return words


#分词后词性的处理（将处理的generator 处理成为 list 再有list方式转化为 dict（））

def gentodict(data):
    list1 = []
    list2 = []
    result = {}
    for word,flag in data:
        list1.append(str(word))
        list2.append(str(flag))
        result = dict(zip(list1,list2))
    return  result
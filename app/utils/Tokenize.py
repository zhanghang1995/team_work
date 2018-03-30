# 使用jieba分词进行词汇Tokenize

import jieba

def tokenize_Full_Word(data):
    seg_list = jieba.cut(data,cut_all=True)
    print("Full Mode: " + "/ ".join(seg_list))  # 全模式

def tokenize_Word(data):
    seg_list = jieba.cut(data, cut_all=False)
    print("Full Mode: " + "/ ".join(seg_list))  # 精确模式

def tokenize_Search_Word(data):
    seg_list = jieba.cut_for_search(data)  # 搜索引擎模式
    print(", ".join(seg_list))
import json
#判断当前词分量是否为时间
def isTimeWord(data_key):
    if data_key == 't':
        return True


#判断当前词分量是否为人物
def isPeopleWord(data_key):
    if data_key == 'nr':
        return True

#判断当前词分量是否为地点
def isPlaceWord(data_key):
    if data_key == 'ns':
        return True

#判断当前词分量是否为名词
def isNounWord(data_key):
    if data_key == 'n':
        return True


#判断当前词分量是否为人称代词(你，我，他，什么)
def isPronounWord(data_key):
    if data_key == 'n':
        return True

#判断当前词分量是否为动词
def isNounWord(data_key):
    if data_key == 'v':
        return True

#判断当前字符串是否包含字串
def isChildString(father,child1,child2):
    result = child1 in father or child2 in father
    return result

#判断当前字符串是否包含字串
def isSonString(father,child1):
    result = child1 in father
    return result

#对当前字符串进行分割，分割方式按照指定的格式，并返回分割后的列表
def splitString(father,splittype):
    result = father.split(splittype)
    return result


#json处理01版，返回json的数据
def return_json(returnData,dishType,isEnd,type,type2,order):
    result = {"returnData":returnData,"dishType":dishType,"isEnd":isEnd,"type":type,"type2":type2,"order":order}
    resultJson = json.dumps(result,ensure_ascii=False)
    return  resultJson
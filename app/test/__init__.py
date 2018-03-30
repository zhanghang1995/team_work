#用于测试使用
from app.utils.WordTag import possegation


data = possegation("北京天气如何")

list_data = []
for key in data:
    #只先提提取出用户的名词和动词
    print(key + ":" + data[key])
    if data[key] == 'ns':
        if key is not None:
            list_data.append(key)
print(list_data[0])



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
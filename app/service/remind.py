#用于用户的主动提醒测试(早、中、晚的提醒服务),用户服务类
from app.utils.classification import isChildString,splitString,isSonString
from app.utils.wordTag import possegation
from app.utils.classification import return_json
from app.utils.navieBayesClassifier import preprocess,pretokenize,modeal_train
import json
import re
def sevice_deal(data):
# 起床服务的处理方法
    if data['type'] == 0:
        if data['userwords'] == '起床':
            content = return_json("老大，该起床了！", None, False, 0, 0, 0)
            return content
        #已经起床
        elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "起床了":
             # 告诉服务器会话结束
            content = return_json("好样的，老大！", None, True, 0, 0, 0)
            return content
        #等会叫我起来
        elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "等会叫我起来":
            content = return_json("以后几点叫你呢？", None, False, 0, 0, 0)
            return content
        elif re.match(r'[1-9]\d*', data['userwords']):
            # 将时间保存存放数据库中，并通知服务器结束
            # 将时间保存存放数据库中，并告诉服务器会话结束
            if isSonString(data['userwords'], "半"):
                data_result = splitString(data['userwords'], "点")
                result = "0"+data_result[0] + ":30"
            else:
                data_result = splitString(data['userwords'], "点")
                result = "0"+data_result[0] + ":00"
            content = return_json("好的,老大，我"+data['userwords']+"叫你", result, True, 0, 2, 0)
            return content
        else:
            content = return_json("老大，再说一遍，我没听清", None, False, 0, 0, 0)
            return content
# 早饭服务的处理方法
    elif data['type'] == 1:
        if data['hasOrder'] == True:
            if data['userwords'] == '早饭服务':
                # 此处已经记录用户的信息，再次激活直接推送。（判断昨天是否订餐）
                content = return_json("老大，要来一份昨天的早饭吗？", None, False, 1,0,0)
                return content
            #好的 早饭服务
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "好的":
                # 根据用户订餐习惯，响应用户的判断（肯定），获取菜单名称，存入数据库进行订餐服务
                content = return_json("好的，马上去办", None, True, 1,0,1)
                return content
            #换套餐
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "换套餐":
                # 根据用户订餐习惯，响应用户的判断（否定）
                content = return_json("好的，那就换大娘水饺可以吗？", "排骨米饭", False, 1,1,0)
                return content
            else:
                content = return_json("老大，再说一遍，我没听清", None, False, 1, 0,0)
                return content
        else:
            if data['userwords'] == '早饭服务':
                # 第一次服务时候激活提醒
                content = return_json("老大，早饭时间快到了，你想吃点什么？",None,False,1,0,0)
                return content
            #不想吃
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "不吃":
                # 告诉服务器会话结束
                content = return_json("早饭可是精神食粮，在忙也要吃，老大", None, True, 1,0,0)
                return content
            #等会提醒
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "稍后提醒":
                content = return_json("老大，几点提醒你呢？", None, False, 1,0,0)
                return content
            elif re.match(r'[1-9]\d*', data['userwords']):
                # 将时间保存存放数据库中，并告诉服务器会话结束
                if isSonString(data['userwords'], "半"):
                    data_result = splitString(data['userwords'], "点")
                    result = "0"+data_result[0]+":30"
                else:
                    data_result = splitString(data['userwords'], "点")
                    result = "0"+data_result[0]+":00"
                content = return_json("好的，老大，我" + data['userwords'] + "提醒你", result, True, 1,2,0)
                return content
            #想吃什么
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "想吃":
                # 此处识别用户回答想吃内容，进行识别并将内容传递给前台进行存储
                dishes = splitString(data['userwords'], "吃")
                content = return_json("好的，我这就去定" + dishes[1], dishes[1], True, 1,1,1)
                return content

            else:
                content = return_json("老大，再说一遍，我没听清", None, False, 1, 0, 0)
                return content

# 日程安排的处理方法
    elif data['type'] == 2:
        if data['userwords'] == '日程安排':
            content = str("主人，今天准备干什么？")
            return content
        else:
            # 将时间保存存放数据库中，并告诉服务器会话结束
            content = str("已为您记录a结束")
            return content

#午餐服务
    elif data['type'] == 3:
        if data['hasOrder'] == True:
            if data['userwords'] == '午饭服务':
                # 此处已经记录用户的信息，再次激活直接推送。（判断昨天是否订餐）
                content = return_json("老大，中午还吃昨天一样的套餐吗？", None, False, 3,0,0)
                return content
            #好的，可以
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "好的":
                # 根据用户订餐习惯，响应用户的判断（肯定），获取菜单名称，存入数据库进行订餐服务
                content = return_json("好的，马上去办", None, True, 3,0,1)
                return content
            #换套餐
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "换套餐":
                # 根据用户订餐习惯，响应用户的判断（否定）
                content = return_json("好的，那就换排骨饭可以吗？", "排骨米饭", False, 3,1,0)
                return content
            else:
                content = return_json("老大，再说一遍，我没听清", None, False, 3, 0,0)
                return content
        else:
            if data['userwords'] == '午饭服务':
                # 第一次服务时候激活提醒
                content = return_json("老大，吃饭时间快到了，你想吃点什么？",None,False,3,0,0)
                return content
            #不想吃
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "不吃":
                # 告诉服务器会话结束
                content = return_json("在忙也要吃饭，老大", None, True, 3,0,0)
                return content
            # 等会吃
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "稍后提醒":
                content = return_json("老大，几点提醒你呢？", None, False, 3,0,0)
                return content
            elif re.match(r'[1-9]\d*', data['userwords']):
                # 将时间保存存放数据库中，并告诉服务器会话结束
                if isSonString(data['userwords'], "半"):
                    data_result = splitString(data['userwords'], "点")
                    result = data_result[0]+":15"
                else:
                    data_result = splitString(data['userwords'], "点")
                    result = data_result[0]+":00"
                content = return_json("好的，老大，我" + data['userwords'] + "提醒你",result, True, 3,2,0)
                return content
            # 想吃什么
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "想吃":
                # 此处识别用户回答想吃内容，进行识别并将内容传递给前台进行存储
                dishes = splitString(data['userwords'], "吃")
                content = return_json("好的，我这就去定" + dishes[1], dishes[1], True, 3,1,1)
                return content
            else:
                content = return_json("老大，再说一遍，我没听清", None, False, 3, 0, 0)
                return content
#午觉提醒
    elif data['type'] == 4:
        if data['userwords'] == '午觉提醒':
            content = str("主人，中午啦，该睡觉了")
            return content
        elif data['userwords'] == '好的' or data['userwords'] == '马上就睡':
            # 告诉服务器会话结束
            content = str("好样的a结束")
            return content
        elif data['userwords'] == '睡不了了' or data['userwords'] == '等会睡':
            content = str("那你一定要记得午休哟+结束")
            return content
        else:
            content = str("我没听清楚你说什么")
            return content
#晚饭提醒服务
    elif data['type'] == 0:
        if data['hasOrder'] == True:
            if data['userwords'] == '晚饭服务':
                # 此处已经记录用户的信息，再次激活直接推送。（判断昨天是否订餐）
                content = return_json("老大，晚上还吃昨天一样的套餐吗？", None, False, 5,0,0)
                return content
            #好的
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "好的":
                # 根据用户订餐习惯，响应用户的判断（肯定），获取菜单名称，存入数据库进行订餐服务
                content = return_json("好的，马上去办", None, True, 5,0,1)
                return content
            #换套餐
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "换套餐":
                # 根据用户订餐习惯，响应用户的判断（否定）
                content = return_json("好的，那就换排骨饭可以吗？", "排骨米饭", False,5,1,0)
                return content
            else:
                content = return_json("老大，再说一遍，我没听清", None, False, 5, 0,0)
                return content
        else:
            if data['userwords'] == '晚饭服务':
                # 第一次服务时候激活提醒
                content = return_json("老大，晚饭想吃什么？",None,False,5,0,0)
                return content
            #不想吃
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "不吃":
                # 告诉服务器会话结束
                content = return_json("在忙也要吃饭，老大", None, True, 5,0,0)
                return content
            #等会吃
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "稍后提醒":
                content = return_json("老大，几点提醒你呢？", None, False, 5,0,0)
                return content
            elif re.match(r'[1-9]\d*', data['userwords']):
                # 将时间保存存放数据库中，并告诉服务器会话结束
                if isSonString(data['userwords'], "半"):
                    data_result = splitString(data['userwords'], "点")
                    result = str((int(data_result[0])+12))+":30"
                else:
                    data_result = splitString(data['userwords'], "点")
                    result = str((int(data_result[0])+12))+":00"
                content = return_json("好的，老大，我" + data['userwords'] + "提醒你", result, True, 5,2,0)
                return content
            #想吃什么
            elif modeal_train().classify(preprocess(pretokenize(data['userwords']))) == "想吃":
                # 此处识别用户回答想吃内容，进行识别并将内容传递给前台进行存储
                dishes = splitString(data['userwords'], "吃")
                content = return_json("好的，我这就去定" + dishes[1]+"饭", dishes[1], True, 5,1,1)
                return content
            else:
                content = return_json("老大，再说一遍，我没听清", None, False, 5, 0, 0)
                return content
    elif data['type'] == 11:
        words = possegation(data['userwords'])
    else:
        content = json.dumps({"error_code": "1001"})
        return content
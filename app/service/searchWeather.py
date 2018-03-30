#用于天气查询的API接口

from urllib import parse,request
from app.utils.constant import WEATHER_URL,WEATHER_KEY
import json
def seweather(city):
    list = []
    textmod={'key':WEATHER_KEY,'city':city,'output':'json'}
    textmod = parse.urlencode(textmod)
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    req = request.Request(url='%s%s%s' % (WEATHER_URL,'?',textmod),headers=header_dict)
    res = request.urlopen(req)
    res = res.read()
    data = res.decode(encoding='utf-8')
    result = json.loads(data)
    print(result)
    print(result['status'])
    print(result['count'])
    print(result['info'])
    # print(result_data['words_result'])
    for result in result['lives']:
        province = result['province']
        city = result['city']
        weather = result['weather']
        temperature = result['temperature']
        list.append(province)
        list.append(city)
        list.append(weather)
        list.append(temperature)
    print(list)
    return list



# seweather("南京")
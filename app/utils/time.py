#用于获取系统的当前时间，根据对应的时间对用户进行推送服务
import time

#获取系统
def get_time():
    return time.strftime("%Y-%m-%d",time.localtime(time.time()))

#时间区间的比较函数
def compare_time(l_time, start_t, end_t):
    s_time = time.mktime(time.strptime(start_t, '%Y%m%d%H%M'))  # get the seconds for specify date
    e_time = time.mktime(time.strptime(end_t, '%Y%m%d%H%M'))
    log_time = time.mktime(time.strptime(l_time, '%Y-%m-%d %H:%M:%S'))
    if (float(log_time) >= float(s_time)) and (float(log_time) <= float(e_time)):
        return True
    return False


print(time.time())
print(time.localtime(time.time()))
print(time.strftime("%Y-%m-%d",time.localtime(time.time())))
print(time.strftime('%H:%M:%S',time.localtime(time.time())))
if time.strftime('%H:%M:%S',time.localtime(time.time())) < '10:10:10':
    print("YES")
else:
    print("NO")
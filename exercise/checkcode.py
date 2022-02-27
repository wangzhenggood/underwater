import math
import random
from calendar import calendar

if __name__ == '__main__':
    checkcode =''                        #生成一个字符集  otlmeewxd
    for i in range(6):
        print("i",i)
        index = random.randint(0,10)
        print("index:",index)
        if index > i :
            checkcode += chr(random.randint(90, 115))    #chr 将数字转换成对应的ascal码字符
            print("checkode",checkcode)
        elif index < i:
            checkcode += chr(random.randint(66, 90))
            print("checkode",checkcode)
        else:
            checkcode +=str(random.randint(1,9))
            print("checkcode",checkcode)
    print("验证码：", checkcode+checkcode)
print ("随机点数",random.uniform(20, -10))  # 用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限。
print("获取一个随机值",random.randrange(10, 100, 5))  #按指定基数递增的集合中 获取一个随机数。
print("在其中选择任意一个数字",random.choice(("JGood", "is", "a", "handsome", "boy")))    #字典不可以 在其中随机选取一个数
print("随机去掉一个数字",random.choice('abcdefg&#%^*f'))    #随机去一个数字
print("随机取三个数",random.sample('abcdefghij',3) )       #随机取三个数字
print(type(random.sample('abcdefghij',3)))
print("随机取一个数",random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] ))   #lemon



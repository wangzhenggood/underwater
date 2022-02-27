import datetime
mot =['你和我的夏天',
      '为什么你不在',
      '这三丰你快回来',
      '我还有好多话要给你讲啊？']
day=datetime.datetime.now().weekday()
for i in mot:
    print(i)
n=0                #加入列表索引
for n in range(0,len(mot)):
 print(mot[n],day)
 n+1

day1=datetime.datetime.now()  #显示当前时间
print(day1)

print(' '*3,'秋词')
verse=['天晴设在等烟雨','我言秋日胜春朝','晴空一鹤排云上','便引诗情到碧霄']
verse[0]='自古逢秋悲寂寥'             #修改列表中的元素
verse.append('这刘禹锡的《秋词》')
# for i in verse:
#     print(i)
for index,i in enumerate(verse):    #遍历打印索引和列表
    if index%2==0:
        print(i+',' ,end='')
    else:
        print(i+'.')


# motr1=mot.insert('yongyanyi')[1]
# print(motr1)
verse.extend(mot)   #extend 一个列表的所有内容追加到另一个列表
print(verse)

from datetime import datetime
now = datetime.now() # current date and time
print('datanow:',now)
year = now.strftime("%Y")
print("year:", year)
month = now.strftime("%m")
print("month:", month)
day = now.strftime("%d")
print("day:", day)
time = now.strftime("%H:%M:%S")
print("time:", time)
date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
print("date and time:",date_time)
#list=[Expression for var in range]
#Expression 表达式 用来计算新列表的元素
#var 循环变量
#range 查用range函数生成的range对象
import random      #列表推导式
fandomnumber=[random.randint(10,100)for i in range(10)]
print(fandomnumber)
a=sorted(fandomnumber)   #使用函数升序
print(a)
b=sorted(fandomnumber,reverse=True)   #降序排列
print(b)
fandomnumber.sort() #升序排列   调用方法
print(fandomnumber)
price=[1000,2000,2222,5111,3000,1542]
sale=[int(x*0.5)for x in price]
print('打折后的价格：',sale)
price=[1000,2000,2222,5111,3000,1542]
sale1=[x for x in price if x>2450]
print('大于2450的数字：',sale1)
print('===========================')
arr=[]
for i in range(5):
    arr.append([])
    for j in range(5):
        arr[i].append(j)
print('arr：',arr)
arr=[[j for j in range(5)] for i in range(4)]   #同上
print(arr)
s=arr[1][2]  #列表下标  从0开始
print(s)
a=['aaa','vvv','ccc','ccv','ccc','ccc','ccc','sss','ddd']
for index,i in enumerate(a):                                     #enumerate 枚举
    print(index,i)
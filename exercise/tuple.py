# 元组中的元素是不可修改的，是一个不可变的序列，可以将任何类型的内容放入其中
import random
verse=('这是一个美丽的冬天',)   #·····························加 ， 表示定义一个元组
print(verse)
print(type(verse))

verse1=('这是一个美丽的冬天')   #   不加 ，表示定义一个字符串
print(verse1)
print(type(verse1))

verse2=tuple(range(1,20,3))  #tuple
print(verse2)
print(type(verse2))

# del verse2
# print(verse2)   #以删  找不到verse2元组

print(verse2[:3])   #访问前三个
print(verse2[3:])   #访问第三个之后的
print(verse2[-3:])  #访问最后三个

us=verse+verse2  #只有同是元组时才可以连接
print(us)

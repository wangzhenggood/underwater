import random

# random.randint随机产生一个1到100的数
randomdict = {i: random.randint(1, 200) for i in range(1, 10)}  # 使用字典推导式
print(randomdict)

setdic = {'www', 'zzz', 'hhh', 'mmm', 'ggg', 'ggg', 'aaa'}  # 集合用于保存不重复的元素  如果有重复的元素则去重
print(setdic)  # 并且保存的元素是无序的

A = set(['WWW', 'ZZZ', 'XXX', 'CCC', 'AAA'])

B = set(('ASD', 'ADSD', 'ASD', 'ASD', 'ASD', 'ASSD', 'ASSD'))
C = set('WANGZHENG')
print('A', A)  # 使用set函数将字符串 列表 元组 创建成集合 并去重
print(B)
print(C)

a = set()  # 创建的空集合
a.add('wanz')  # 集合只能添加一个元素
print(a)

D = A.pop()  # 找到集合的一个元素
print('d', D)
#
# f=A.pop()
# print(f)

# c=set(B).clear()  #clear（）清空集合
# print(c)

#  交集：&   并集：|   差集：-  对称差集：^

print(A | B)

S = {i for i in range(1, 30)}
print(S)
# S={1, 2, 3, 4, 5, 6, 7, 8, 9}
# del命令删除集合    pop（）方法或者remove（）方法删除一个元素   clear（）清空集合
S.remove(29)  # 选择删除
print(S)
S.pop()  # 删除第一个
print(S)
# S.clear()
# print(S)   #删除集合内的值
# del(S)       #删除集合
# print(S)
f = list(S)
print(f)

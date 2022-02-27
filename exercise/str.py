verse='野渡无人舟自横'
byte=verse.encode("UTF-8")
print(verse)
print(byte)

verse1=byte.decode("UTF-8")
print(verse1)

a=len(verse)
print(a)

b='人 生 苦短我用python'
a1=b[1]                  # :  代表其内的数字
a2=b[2:]
a3=b[:3]
a4=b[4:6]
try:
    a5=b[100]
except:
 print('索引不存在')
print('a1:',a1,'\n','a2:',a2,'\n','a3:',a3,'\n','a4:',a4,'\n')

b1=b.split()
b2=b.split('我')            #split 选择的那个字符串进行分割 字符串分隔符的使用
b3=b.split('p',5)
print(b1,'\n',b2,'\n',b3)
print(b.split('用')[1],)
print(b.count('t'))
print(b.find('我'))  #返回索引    rfind  从右边开始寻找
print('ni' in b)
print(b.index('我'))  #rindex
print(b.startswith('用'),b.endswith('thon'))

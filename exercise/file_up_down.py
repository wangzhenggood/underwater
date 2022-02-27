print('+'*10,'真好','+'*10)
file=open('message.txt','w' ,encoding='utf-8')       #建立一个同路径下的txt文件 r 只读 定位到文件的开头，必须有文件，才能进行操作
print('\n 即将显示 \n')                                #a 定位到文件的结尾，进行追加  如果没有文件就创建一个文件

file.write('学习一门编程语言一般从基础的数据类型开始 ，python中的数据类型有：整型、浮点、布尔、字符串、\n列表、元组、字典、集合、空等，之前总结了一些字符串的操作和应用，希望能帮到学习python的朋友们。')
#file.close()                                          #关闭文件 后无法操作 操作后报错
file.write('split（）切割功能，切割后 形成的是列表。\n按照特定内容切割，‘’引号里可以是空格、字符(默认是空格）\n 可以指定切割次数可以从右面切割按行切割,换行符切割')
file.close()
file=open('message.txt','a',encoding='utf-8')
file.write('strip(）默认删除行首或者行尾的空白符（包括’\n’, ‘\r’, ‘\t’, ’')
file.close()                                       #只有关闭文件，文件才能保存，否则文件仅仅保存在缓存中

with open('message.txt','r',encoding='utf-8') as file:     #打开文件
    string=file.read(10)                                   #读取文件前10个字符
    print(string)
file.close()

with open('message.txt','r',encoding='utf-8') as file:
    file.seek(6)                                          #打开文件从第三个开始取值
    string=file.read(6)                                   #取六个字符
    print(string)

with open('message.txt','r',encoding='utf-8') as file:   #答应全部内容
    number=0
    while True:
        number+=1
        line=file.readline()
        if line=='':
            break
        print(number,line,end='\n')
    print('='*30,'over','='*20)

with open('message.txt','r',encoding='utf-8') as file:  #以一个列表的方式打印全部内容
    message=file.readlines()
    print(message)

a=[1, 2, 3, 4, 5]
sums = sum(map(lambda x: x + 3, a[1::3]))          #lambda 匿名函数  相当于 def
print(sums)                          #第一个参数接受一个函数名，后面的参数接受一个或多个可迭代的序列，返回的是一个集合。
                                 #把函数依次作用在list中的每一个元素上，得到一个新的list并返回。注意，map不改变原list，而是返回一个新list。

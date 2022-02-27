import os
os.name
print(os.name)                                             #nt windows系统  posix Linux Unix macos
print(os.sep)                                              #打印换行符
print(os.getcwd())                                         #打印当前路径目录
#print(os.listdir('D:\study_007\exercise'))                #返回指定目录下的文件
#print(os.mkdir("D:\study_007\exercise['xingjian']"))      创建目录
#os.dir(os.getcwd()+"exercise['xingjian']")                删除目录
a=os.path.abspath('study_007')                             #获取文件的绝对路径
print(a)
with open('message.txt' ,'r',encoding='utf-8')as file:
     message = file.readlines()
     print(message)

print(os.path.join('D:\study_007\exercise','demo\code'))    #目录拼接
'''tuples=os.walk("D:\study_007")                           #遍历目录
for i in tuples:
    print(i,'\n')'''

fiel=os.stat('lover_fever.py')
print(os.path.abspath('lover_fever.py'))                    #绝对路径
print(fiel.st_ino)                                          #索引号
print(fiel.st_size)                                         #大小
print(fiel.st_atime)                                        #最后一次访问时间

#os.rmdir("D:/study_007/exercise/link_Mysql")               #删除空目录
import os
def formatTime(longtime):
    '''格式化日期时间函数
    longtime 要格式化的时间
    '''
    import time
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(longtime))           #localtime   当地时间   time.localtime(longtime）读取最近打开时间
def formatByte(number):                                                         #strftime  时间格式
    '''格式化文件大小的函y数
    number：要格式的字节数
    '''
    for (scale,label) in [(1024*1024*1024,'GB'),(1024*1024,'MB'),(1024,'KB')]:         #label ：标签 scale ：规模
        if number>=scale:
            return '%.2f%s'%(number*1.0/scale,label)                      #   % 替换的内容放在字符串后面的%后面
        elif number ==1:
            return '1  字节'
        else:
            byte='%.2f'%(number or 0)
    return  (byte[:-3] if byte.endswith('.00')else byte)+'字节'

if __name__ == '__main__':
    fiel = os.stat('lover_fever.py')
    print(os.path.abspath('lover_fever.py'))  # 绝对路径
    print(fiel.st_ino)  # 索引号
    print('size',formatByte() ) # 大小
    print('time',formatTime(fiel.st_atime) ) # 最后一次访问时间

    fiel1 = os.stat('lover_fever.py')
    print(os.path.abspath('lover_fever.py'))  # 绝对路径
    print(fiel1.st_ino)  # 索引号
    print('size',fiel1.st_size)  # 大小
    print('time',fiel1.st_atime)  # 最后一次访问时间
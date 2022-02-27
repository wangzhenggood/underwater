def function_tips():
    '''功能每天输出一条励志文字'''
    import datetime
    #定义一个列表
    mot = ['好好感受这个世界',
           '好好爱这个世界',
           '扭力',
           '加油',
           '好的',
           '可以',
           'why I dont know']
    day = datetime.datetime.now().weekday()
    print(mot[day])

function_tips()
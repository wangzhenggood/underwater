class Geese:
    def __init__(self,face,eye,hand):
        print('我是大帅哥,我有：')
        print(face,end='   ')
        print('\t',eye,end='   ')
        print('\t',hand+'   我是最棒的')
face_1 ='帅气的脸'                          #把face_1 eye_1  hand_1     传递到类中
eye_1='明亮的眼睛'
hand_1='坚硬的手臂'
man=Geese(face_1,eye_1,hand_1)             #使用类中的方法进行输入
print()
print()

class geese:
    neck='大眼睛'
    wind='高鼻梁'
    leg='翘首以待'
    number=10
    def __init__(self):
        geese.number+=1
        print(str(geese.number),'我是最帅的哥')
        print(geese.neck+'整的')
        print(geese.wind)
        print(geese.leg)
geese()
list1=[]
for i in range(5):
    list1.append(geese())
    print(geese.number)
a=geese()            #实例化一个对象   
class Geese:
    '名人'
    pass           #没有想好具体的功能，可以用pass代替
class Rect:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        print('long'*3)
    @property
    def area(self):
        return self.height*self.width
reet=Rect(10,20)
print(Rect(10,20).area)

class Fruit:
    color='绿色'
    def harvest(self,color):
        print('水果是：',Fruit.color)   #引用自己的类属性 绿色
        print('水果原来是',color)        #
class Apple(Fruit):
    color = '红色'                #类属性进行传参
    def __init__(self):
        print('我是苹果')
class Orange:
    color='红色'
    def __init__(self):
        print('我是梨子')
apple=Apple()
apple.harvest(Apple().color)    #color传参给父类Fruit harvest
orange=Orange()



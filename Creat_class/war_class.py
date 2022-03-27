import time
class role():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def tong(self,enemy):
        enemy.hp-=1000
        info="%s 捅了 %s一刀" % (self.name,enemy.name)
        print(info)

    def kan(self,enemy):
        enemy.hp-=1500
        info="%s 捅了 %s一刀 " % (self.name,enemy.name)
        print(info)

    def chiyao(self,enemy):
        enemy.hp+=100
        info = "%s 加了10滴血" % (self.name)
        print(info)
    def qiangji(self,enemy):
        enemy.hp-=1000
        info="%s 暴击kill %s" % (self.name,enemy.name)
        print(info)
    def __str__(self):
        return '%s 还剩 %s 的血量' % (self.name , self.hp)

wz=role('王政',100000)
zhm=role('曾红梅',90000)
i=0
while True:
    if wz.hp<=50 or zhm.hp<=50:
        break
    i+=1
    print()
    print("第%s回合.............." %(i))
    wz.kan(zhm)
    print(zhm)
    zhm.tong(wz)
    print(wz)
    zhm.kan(wz)
    print(wz)
    wz.chiyao(wz)
    zhm.qiangji(wz)
    print(wz)
    wz.qiangji(zhm)
    print(zhm)
    wz.chiyao(wz)
    print(wz)
    zhm.chiyao(zhm)
    print(zhm)
    zhm.tong(wz)
    print(zhm)
    zhm.qiangji(wz)
    print(wz)
print("战斗结束........................")
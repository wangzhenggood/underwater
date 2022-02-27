i = 10
HuiWenSu =[]
JieGuo = []
 #筛选回文数
while i <= 1000:
     ZiFu = str(i)
     FanZhuan = ZiFu[::-1]
     HuiWen = int(FanZhuan)
     if HuiWen == i:
        HuiWenSu.append(HuiWen)
     i += 1
 #在筛选出来的回文数中筛选符合条件的素数
for Hui in HuiWenSu:
     a = 2
     while a < Hui:
         if Hui % a == 0:
             break
         elif a+1 == Hui:
             JieGuo.append(Hui)
             a += 1
         else:
             a += 1

print(JieGuo)
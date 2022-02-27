
'''for i in range(1,10):    #九九乘法表    外循环循环，第一次，内循环循环一次，并打印结果，外循环依此遍历九次，内循环在外循环遍历九次的过程中
    for j in range(1,i+1):       #内循环每一次循环都打印，依此循环完毕，进入外循环
        print(str(j),'x',str(i),'=',str(i*j),'\t',end='   ')  # \t 对齐     end=''  打印不换行
    print() #打印换行'''


for i in range(1,10):
    for j in range(1,i+1):
        print(str(j),'x',str(i),'=',str(i*j),'\t',end='   ')
    print()
print()
print()
for i in range(100,1000):
    b=i//100                           # //整除
    s=i//10%10                         # %取余
    g=i%10
    if i==b*b*b+s*s*s+g*g*g:
        print(i)

print(123//10%10)
print(123//100)
print(123%10)
#递归
#RecursionError: maximum recursion depth exceeded while calling a Python object
#最大递归错误最多1000
def func1(x):
    print(x)
    func1(x-1)

def func2(x):
    if x>0:
        print(x)
        func2(x+1)
def func3(x):
    if x>0:
        print(x)
        func3(x-1)
def func4(x):
    if x>0:
        func4(x-1)
        print(x)
#================================================================
#汉诺塔问题
def hanni(n,a,b,c):
    if n>0:
        hanni(n-1,a,c,b)
        print(a,"to",c)
        hanni(n-1,b,a,c)

#顺序查找方法
def liner_search(li,val):
    for ind , v in enumerate(li):
        if v == val :
            return ind
    else:
        return None
def binary_search(li,val):
    left=0
    right = len(li)-1
    while left <= right:
        mid =(left + right) //2
        if li(mid) == val:
            return mid
        elif li(mid) > val:
            right = mid - 1
        else:
            left = mid + 1
    else:
        return None

if __name__ == '__main__':
    #func1(3)
    #func2(3)
    #func3(4)
    print("-------------------")
    #func4(5)
    hanni(5,'a','b','c')
def func3(x):
    if x >0:
        print(x)
        func3(x-1)
def func4(x):
    if x>0:
        func4(x-1)
        print(x)

if __name__ == '__main__':
    func3(4)
    func4(4)

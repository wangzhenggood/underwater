import re
pattern=r'(13[4-9]\d{8})$|(15[01289]\d{8})$'
mobile=input('请输入11位电话号码;')
match = re.match(pattern,mobile)
if match ==None:
    print('不是有效的')
else:
    print('可以的，就是这样')

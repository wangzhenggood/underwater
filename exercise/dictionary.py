name=['王','周','罗学','蒲','朱','苏']
sign=['wangzheng','zouhui','luoxuew','pubo']#,'zhuxing','suchuangeng','www']
dictionnary=dict(zip(name,sign))
print(dictionnary)

dictionnary2={'王政':'a','王伟':'b','王狗':'a','王大':'c'}
print(dictionnary2)

dictionnary3=dict(A='王',B='王y',C='王er',D='王s',F='王w')
print(dictionnary3)
 
name1=['王','周','罗学','博','朱','苏']
#sign=['wangzheng','zouhui','luoxuew','pubo','zhuxing','suchuangeng','www']
dictionnary4=dict.fromkeys(name1)
print(dictionnary4)

# del dictionnary3
# dictionnary3=dict(A='王政',B='王政',C='王政',D='王政',F='王政')
# print(dictionnary3)

dictionnary.clear()
print(dictionnary)

print(dictionnary3['A'])

print(dictionnary3.get('B')) ######################################################
print(dictionnary3.get('www'))  #若是没有则返回none
print(dictionnary3.get('www','的确没有这个人'))

for item in dictionnary3.items():  #items 遍历键值对
    print(item)

for item in dictionnary3:#.items():  #items 遍历键
    print(item)

for item,item1 in dictionnary3.items():  #items 遍历键值对
    print(item,item1)

if 'E' in dictionnary3:    #防止删除不存在的元素，抛出异常
    del dictionnary3['E']
print(dictionnary3)


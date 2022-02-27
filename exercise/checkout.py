def fun_checkout(money):
    money_old=sum(money)     #计算和
    money_new=money_old
    if money_old>=500 and money_old<1000:             # '{:.2f}'.format | ‘%.2f’ % num 两个都为保留小数后两位
        money_new='{:.2f}'.format(money_old*0.9)
    elif money_old>=1000 and money_old<=2000:
        money_new='{:.2f}'.format(money_old*0.8)
    elif money_old>=2000 and money_old<=3000:
        money_new='{:.2f}'.format(money_old*0.7)
    elif money_old>=3000 :
        money_new='{:.2f}'.format(money_old*0.6)
    return money_old ,money_new

if __name__ == '__main__':
    print('开始结算,,,,,,')
    list_money=[]
    while True:                                          #
        inmoney=float(input('请输入商品金额，输入n结束：'))
        if int(inmoney) == 0:
            break
        else:
            list_money.append(inmoney)           #将元素追加列表的最后
    print(list_money)
    money=fun_checkout(list_money)               #调用定义的方法
    print(money)
    print('合计金额：',money[0],'应付金额:',money[1])
    print(list_money)





m = int(input("请输入月份："))

if m in (1, 3,  5, 7, 8, 10, 12):
    print(f"{m}月有31天")
elif m == 4 or m == 6 or m == 9 or m == 11:
    print(f"{m}月有30天")
elif m == 2:
    y = int(input("请输入年份："))
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(f"{y}年是闰年，2月有29天")
    else:
        print(f"{y}年是平年，2月有28天")
else:
    print(f"输入的月份【{m}】无效，必须是1到12之间的数字")

print("\n程序结束！")
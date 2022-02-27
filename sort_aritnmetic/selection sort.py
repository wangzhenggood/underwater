# a=[6,5,3,4,10,12,7,24,2,1]
# min_index=0
# for i in range(len(a)-1):
#     min_index=i    #每次i变化时，将最小下标值改为i，将本次循环第一个位置的值
#     for j in range(i+1,len(a)):#和当前i元素之后的所有值进行比对
#         if a[min_index]>a[j]:
#             min_index=j#如果发生小于的情况，则把此数的坐标赋值于min_index
#     #当所有数比较完毕之后，将i坐标值和当前循环找到的最小值进行交换
#     a[i],a[min_index]=a[min_index],a[i]
# print(a)
#
# b=[100,20,50,30,15,34,6,5,66,5,68,46,60]
# print(sorted(b))
# for i in range(len(b)-1):
#     min_index1 = i
#     for j in range(i+1,len(b)):
#         if b[min_index1]>b[j]:
#             min_index1=j
#     b[i],b[min_index1]=b[min_index1],b[i]
# print(b)

# c = 10
# d = 15
# c,d =d,c
# print(c,d)

nums=[10,25,24,25,57,35,64,95,105,65,56,4,6,10,4,9,9,9,9,4,55,4,64,6,4,645,6,4,21,32468,75,4,6]
#nums=[11,10,9]
for i in range(len(nums)):
    min_dex=i
    for j in range(i,len(nums)):
        if nums[min_dex]>nums[j]:
            min_dex=j
    nums[i],nums[min_dex]=nums[min_dex],nums[i]
print(nums)
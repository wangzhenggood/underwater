'''冒泡排序（Bubble Sort）也是一种简单直观的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。
走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。
作为最简单的排序算法之一，冒泡排序给我的感觉就像 Abandon 在单词书里出现的感觉一样，每次都在第一页第一位，所以最熟悉。冒泡排序还有一种优化算法
，就是立一个 flag，当在一趟序列遍历中元素没有发生交换，则证明该序列已经有序。但这种改进对于提升性能来说并没有什么太大作用。
1. 算法步骤
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。'''
import random
def one():
    arr=[3,2,1,0]

    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            #print(len(arr)-i)
            #print(j)
            print('i:',i,arr[i],'j:',j,arr[j],'——'*9,arr[j],arr[j+1])
            if arr[j] > arr[j+1]:
               arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)

    #for s in range(0,10):
    # print(s)

    print(sorted(arr))
def two(fee):
    for i in range(len(fee)-1):   #定义趟数如果列表理由七个数，实际上只循环6次，最后一次不用在排序了。所以排序次数要减一次。为循6次，从头到尾走六趟
        for j in range(len(fee)-i-1):  #每一趟在其中的循环
            if fee[j] > fee[j+1]:
                fee[j],fee[j+1]=fee[j+1],fee[j]


if __name__ == '__main__':

    j=[random.randint(1,1500) for i in range(100)]
    print(j)
    two(j)
    print(j)

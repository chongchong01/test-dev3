"""
快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为较小和较大的2个子序列，然后递归地排序两个子序列。

步骤为：

挑选基准值：从数列中挑出一个元素，称为"基准"（pivot）;
分割：重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（与基准值相等的数可以到任何一边）。在这个分割结束之后，对基准值的排序就已经完成;
递归排序子序列：递归地将小于基准值元素的子序列和大于基准值元素的子序列排序。
递归到最底部的判断条件是数列的大小是零或一，此时该数列显然已经有序。

选取基准值有数种具体方法，此选取方法对排序的时间性能有决定性影响。

例子：
[6,2,10,5,4,8,7]
1. 选择基准值，假如我们选择第一个值就是6,
2. 把数据分为两块，把比6大的放到右边，把比6小放到左边: 数据就变成了 [2, 5, 4]  6  [10, 8, 7]
如果把左边和右边都看成一个数，那么这三个数是不是已经是有序的了，
所有后面要处理的时候就是，把左边和右边里面的数据都变成有序

3. 然后递归左边 [2, 5, 4]  重新执行 步骤1， 步骤2
    [4] 2 [5]  然后继续递归执行  步骤1， 步骤2
    2 4 5
4. 然后递归右边 [10, 8, 7] 重新执行 步骤1， 步骤2
    [8, 7] 10   然后继续递归执行  步骤1， 步骤2
    7 8 10
"""

# 快速排序函数
def quick_sort(data):
    if len(data) < 2:
        return data

    pivot = data[0] # 基准值

    left = []
    right = []

    for index, item in enumerate(data):
        if 0 == index: # 基准值就略过
            continue

        # 当前元素小于基准值，放到左边
        if item < pivot:
            left.append(item)
        else:  # 当前元素大于等于基准值，放到右边
            right.append(item)

    left = quick_sort(left) # 对应着第三步
    right = quick_sort(right)  # 对应着第四步

    return left + [pivot] + right



arr = [7, 10 , 8, 9, 1, 5, 5]
arr = quick_sort(arr)

print("排序后的数组:")
for i in arr:
    print(i)
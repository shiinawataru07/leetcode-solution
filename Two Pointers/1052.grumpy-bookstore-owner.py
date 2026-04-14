class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        res = cnt = 0
        for right, customer in enumerate(customers) :
            if grumpy[right] == 1 :
                cnt += customer
            left = right - minutes + 1
            if left < 0 :
                continue
            res = max(res, cnt)
            if grumpy[left] == 1 :
                cnt -= customers[left]
        return res + sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)


'''
解析：
可将老板不生气的时间视为一个窗口
考察窗口内覆盖的 老板原本会生气的时间的顾客总数 取到的最大值
最终所有满意的顾客即为 原本就满意的顾客数 以及 通过冷静而使顾客从不满足变得满足的顾客数 的和
使用定长滑动窗口即可求解
'''

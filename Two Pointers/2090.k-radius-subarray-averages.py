class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        left = 0
        right = 2 * k + 1
        mysum = 0
        if right <= len(nums) :
            mysum = sum(nums[left : right])
            avgs[(left + right) // 2] = mysum // (2 * k + 1)
        while right < len(nums) :
            mysum += nums[right]
            right += 1
            mysum -= nums[left]
            left += 1
            avgs[(left + right) // 2] = mysum // (2 * k + 1)
        return avgs


'''
解析：
定长滑动窗口
left与right来对窗口进行维护
我们只考虑在边界范围内的数据的改变
'''

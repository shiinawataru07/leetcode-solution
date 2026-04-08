class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = sum(nums[0:k])
        cnt = res
        left = 0
        right = k
        while right < len(nums) :
            cnt += nums[right]
            right += 1
            cnt -= nums[left]
            left += 1
            res = max(res, cnt)
        return res / k


'''
解析：
简单的定长滑动窗口
right进窗口，left出窗口即可
'''

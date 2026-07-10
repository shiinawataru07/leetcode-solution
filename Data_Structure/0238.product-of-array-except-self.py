class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [num for num in nums]
        suf = [num for num in nums]
        for idx in range(1, n):
            pre[idx] = pre[idx - 1] * nums[idx]
        for idx in reversed(range(n - 1)):
            suf[idx] = suf[idx + 1] * nums[idx]
        ans = [0 for _ in range(n)]
        ans[0] = suf[1]
        ans[n - 1] = pre[n - 2]
        for idx in range(1, n - 1):
            ans[idx] = pre[idx - 1] * suf[idx + 1]
        return ans

'''
朴素方法，维护前缀积与后缀积
时间复杂度o(n)，空间复杂度o(n)
'''

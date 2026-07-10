class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [num for num in nums]
        for idx in range(1, len(nums)):
            dp[idx] = max(0, dp[idx - 1]) + nums[idx]
        return max(dp)


'''
使用dp[i]数组来维护以第i位结尾的子数组的最大和
状态转移方程 dp[i]=max(0, dp[i-1])+dp[i]
时间复杂度o(n)，空间复杂度o(n)
事实上可以通过用用pre和cur来滚动记录dp数组的前一位和现在一位优化空间复杂度

另一种思路：分治，具体参考线段树
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx in range(n):
            if nums[idx] <= 0:
                nums[idx] = n + 1
        for idx in range(n):
            if abs(nums[idx]) <= n:
                nums[abs(nums[idx]) - 1] = -abs(nums[abs(nums[idx]) - 1])
        for idx in range(n):
            if nums[idx] > 0:
                return idx + 1
        return n + 1


'''
我们需求对正整数做标记来判断某个数是否出现过
为了原地哈希，我们只需利用数组的正负来作为标记即可
时间复杂度O(n)
空间复杂度O(1)
'''

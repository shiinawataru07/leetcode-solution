class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        for b in range(1 << len(nums)):
            subset = [x for i, x in enumerate(nums) if b >> i & 1]
            res.append(subset)
        return res

'''
使用二进制来表示每个元素是否在子集中，遍历所有可能的二进制数，从而生成所有子集。
'''

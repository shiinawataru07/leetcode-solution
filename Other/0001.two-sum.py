class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i in range(len(nums)) :
            num = nums[i]
            if num in d :
                return [d[num], i]
            d[target - num] = i

'''
解析：使用哈希表，将查找target-num的复杂度降低
另一方法：暴力枚举两层循环
'''

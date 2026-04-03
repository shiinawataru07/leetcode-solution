class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        res = 0
        myset = set(nums)
        for num in myset :
            if num - 1 not in myset :
                cur = num
                cnt = 0
                while cur in myset :
                    cur += 1
                    cnt += 1
                res = max(res, cnt)
        return res

'''
解析：先特判nums=[]的情况
考察nums当中的所有数，对每个能成为序列开头的数考虑连续序列长度
复杂度达到on
'''

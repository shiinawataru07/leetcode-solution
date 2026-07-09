class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        vis = defaultdict(int)
        vis[0] = 1
        s = [0 for _ in range(len(nums))]
        for idx, num in enumerate(nums):
            if idx == 0:
                s[idx] = num
            else:
                s[idx] = s[idx - 1] + num
            if s[idx] - k in vis:
                ans += vis[s[idx] - k]
            vis[s[idx]] += 1
        return ans


'''
s为前缀和数组
使用vis来记录已经处理过的前缀和的不同数值出现次数
vis[s[idx]-k]也就是s[idx]-k出现过的次数
即为满足s[idx]-s[x]为x到idx的子数组的和等于k的x的个数
'''

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = cur = 0
        mp = collections.defaultdict(int)
        for right, val in enumerate(nums) :
            cur += val
            mp[val] += 1
            left = right - k + 1
            if left < 0 :
                continue
            if len(mp) == k :
                res = max(res, cur)
            cur -= nums[left]
            mp[nums[left]] -= 1
            if mp[nums[left]] == 0 :
                del mp[nums[left]]
        return res


'''
解析：
与t2841相同，定长滑动窗口
出窗时使用mp维护窗口内不同元素数量
每次窗口元素数量等于窗口长度时更新记录
'''

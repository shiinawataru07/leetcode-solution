class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res = cur = 0
        cnt = collections.defaultdict(int)
        for right, val in enumerate(nums) :
            cur += val
            cnt[val] += 1
            left = right - k + 1
            if left < 0 :
                continue
            if len(cnt) >= m :
                res = max(res, cur)
            cur -= nums[left]
            cnt[nums[left]] -= 1
            if cnt[nums[left]] == 0 :
                del cnt[nums[left]]
        return res


'''
解析：
定长滑动窗口，使用cnt来统计窗口内的字符出现数目
在出窗口时维护cnt需要删除hashmap
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = -1
        right = 0
        res = 0
        lastpos = collections.defaultdict(lambda : -1)
        while right < len(s) :
            left = max(left, lastpos[s[right]])
            res = max(res, right - left)
            lastpos[s[right]] = right
            right += 1
        return res
'''
解析：
通过哈希表记录字符最后出现的位置来直接跳跃左指针
右指针逐渐推进实现优化滑动窗口
'''

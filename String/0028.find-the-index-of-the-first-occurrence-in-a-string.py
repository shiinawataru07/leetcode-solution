class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = [-1] * len(needle)
        i, k = 0, -1
        while i < len(needle):
            while k >= 0 and needle[i] != needle[k]:
                k = next[k]
            i += 1
            k += 1
            if i == len(needle):
                break
            next[i] = next[k] if needle[i] == needle[k] else k
        i, j = 0, 0
        while i < len(needle) and j < len(haystack):
            if i == -1 or needle[i] == haystack[j]:
                i += 1
                j += 1
            else:
                i = next[i]
        return j - len(needle) if i == len(needle) else -1

'''
next优化数组 + kmp模式匹配
时间复杂度 O(n+m) 空间复杂度 O(m) 其中 n 为 len(haystack), m 为 len(needle)
'''

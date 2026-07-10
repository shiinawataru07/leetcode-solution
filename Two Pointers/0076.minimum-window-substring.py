class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        need = defaultdict(int)
        for ch in t:
            need[ch] += 1
        window = defaultdict(int)
        def check() -> bool:
            for ch in need:
                if window[ch] < need[ch]:
                    return False
            return True
        l = 0
        ans = ""
        min_len = float("inf")
        for r in range(len(s)):
            window[s[r]] += 1
            while check():
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    ans = s[l:r + 1]
                window[s[l]] -= 1
                l += 1
        return ans

  '''
  使用一个defaultdict来维护t中字符出现的数量
  接下来用双指针l,r来维护s子串的滑动窗口，使用一个defaultdict来维护窗口中字符出现的数量
  如果t中每个字符数量都小于窗口中的数量不成立，那么r++，否则 l++
  时间复杂度o(n*k)

  优化：
  class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        need = defaultdict(int)
        for ch in t:
            need[ch] += 1
        window = defaultdict(int)
        required = len(need)
        formed = 0
        l = 0
        min_len = float("inf")
        ans_l = 0
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
            while formed == required:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    ans_l = l
                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1
        if min_len == float("inf"):
            return ""
        return s[ans_l: ans_l + min_len]

使用formed变量来维护已经达到t中要求的字符数量，required来记录t中不同字符个数
当formed==required时即为窗口中的字符满足t中的字符要求
优化了使用check()函数每次都需要遍历
时间复杂度o(n+m)
'''

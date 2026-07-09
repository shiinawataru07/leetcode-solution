class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dict_p = defaultdict(int)
        dict_s = defaultdict(int)
        ans = list()
        for ch in p:
            dict_p[ch] += 1
        for idx, ch in enumerate(s):
            dict_s[ch] += 1
            if idx >= len(p) - 1:
                if dict_s == dict_p:
                    ans.append(idx - len(p) + 1)
                dict_s[s[idx - len(p) + 1]] -= 1
                if dict_s[s[idx - len(p) + 1]] == 0:
                    del dict_s[s[idx - len(p) + 1]]
        return ans


'''
维护一个滑动窗口，用字典来比较每个窗口内的字符串是否为目标字符串的异位词
'''

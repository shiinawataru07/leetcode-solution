class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        stk = [([], 0)]
        n = len(s)
        while stk:
            path, l = stk.pop()
            if l == n:
                ans.append(path)
                continue
            for i in range(l, n):
                if s[l: i+1] == s[l: i+1][::-1]:
                    stk.append((path + [s[l: i+1]], i+1))
        return ans

'''
dfs 搜索所有回文子串分割的可能性
时间复杂度 O(n^2 2^n)
可以进行回文子串的预处理让时间复杂度降低为 O(n 2^n)
'''

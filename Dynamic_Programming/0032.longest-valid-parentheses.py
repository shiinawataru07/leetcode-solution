class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                else:
                    pos = i - 1 - dp[i - 1]
                    if pos >= 0 and s[pos] == '(':
                        dp[i] = dp[i-1] + 2
                        if pos > 0:
                            dp[i] += dp[pos - 1]
        return max(dp)

'''
使用 dp 维护以 i 为结尾的最长有效括号长度
注意到仅在以')'为结尾时才能构成最长有效括号
讨论前一位来进行状态转移
时间复杂度 O(n) 空间复杂度 O(n)
'''

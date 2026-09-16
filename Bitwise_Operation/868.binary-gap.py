class Solution:
    def binaryGap(self, n: int) -> int:
        last = -1
        pos = 0
        ans = 0
        while n:
            if n & 1:
                if last != -1:
                    ans = max(ans, pos - last)
                last = pos
            n >>= 1
            pos += 1
        return ans


'''
从低位到高位遍历统计
时间复杂度 O(logn) 空间复杂度 O(1)
'''

class Solution:
    def countMonobit(self, n: int) -> int:
        return (n + 1).bit_length()

'''
我们想要统计 n 以内 全为 1 的二进制数个数
也就是说 (n+1) 的二进制位数 - 1，然后再加上 1（因为 0 也满足）即可
时间复杂度 O(1) 空间复杂度 O(1)
'''

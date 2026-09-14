class Solution:
    def concatenatedBinary(self, n: int) -> int:
        dic = set([2**x for x in range(1, 18)])
        flg = 1
        res = 0
        MOD = 10**9 + 7
        for num in range(1, n+1):
            if num in dic:
                flg += 1
            res = ((res << flg) + num) % MOD
        return res


'''
暴力模拟
时间复杂度 O(n), 空间复杂度 O(1)
可以使用数学方法计算公式
时间复杂度 O(logn*(logn+logM)), 空间复杂度 O(1)
其中 M = 1e9 + 7
'''

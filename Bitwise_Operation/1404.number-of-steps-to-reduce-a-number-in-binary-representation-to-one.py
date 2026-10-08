class Solution:
    def numSteps(self, s: str) -> int:
        cnt = len(s) - 1
        i = s.rfind('1')
        if i > 0:
            cnt += s.count('0', 1, i) + 2
        return cnt


'''
公式法：
注意到无论如何都会需要除 n-1 次 2
当碰到 1 时会 +1， 然后产生进位，把前面连续的 1 都变成 0，最近的 0 变成 1
也就是说会让前面有 0 的位置多需要一次 +1，再加上前面的 0 的个数，再算上进位多产生的一次除 2 即可
时间复杂度 O(n) 空间复杂度 O(1)
'''

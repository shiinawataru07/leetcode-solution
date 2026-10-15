class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        j1 = ''.join(sorted([s1[i] for i in range(0, n, 2)]))
        o1 = ''.join(sorted([s1[i] for i in range(1, n, 2)]))
        j2 = ''.join(sorted([s2[i] for i in range(0, n, 2)]))
        o2 = ''.join(sorted([s2[i] for i in range(1, n, 2)]))
        return j1 == j2 and o1 == o2

'''
观察到无论如何做操作，s1 与 s2 的奇数位各字符数和偶数位各字符数都是不变量
'''

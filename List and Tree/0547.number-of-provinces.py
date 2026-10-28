class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = list(range(n))
        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(i1: int, i2: int):
            parent[find(i1)] = find(i2)
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        return sum(parent[i] == i for i in range(n))

'''
并查集模板题
时间复杂度 O(n^2logn) 空间复杂度 O(n)
'''

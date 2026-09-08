class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        x = 0
        y = n-1
        while 0 <= x and x < m and 0 <= y and y < n and matrix[x][y] != target:
            if target < matrix[x][y] :
                y -= 1
            else:
                x += 1
        return 0 <= x and x < m and 0 <= y and y < n and matrix[x][y] == target


'''
我们从右上角开始搜索，我们发现到达矩阵中任意点一定仅经过若干次左移和下移
并且我们发现处于右上角时，下移只排除比原值小的值，左移只排除比原值大的值，
且移动不改变这个性质。
于是我们从右上角开始搜索即可
时间复杂度O(n)，空间复杂度O(1)
'''

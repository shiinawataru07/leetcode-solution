class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        flg_row = 0 in matrix[0]
        flg_col = any(row[0] == 0 for row in matrix)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if flg_row:
            for j in range(n):
                matrix[0][j] = 0
        if flg_col:
            for i in range(m):
                matrix[i][0] = 0



'''
要求使用原地算法来进行矩阵置0，我们可以原地用第一行和第一列来记录行列中有没有0
再单独使用两个变量记录第一行和第一列最初有没有零
时间复杂度O(mn)
空间复杂度O(1)
'''

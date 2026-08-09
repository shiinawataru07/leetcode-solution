class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n-i-1][j] = matrix[n-i-1][j], matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



'''
最朴素的用额外数组来存储的方法显然空间复杂度开销过大
事实上，任何的旋转都可以由若干对称复合而成
于是我们可以用两次对称来模拟顺时针旋转90度
时间复杂度O(n^2)
空间复杂度O(1)
'''

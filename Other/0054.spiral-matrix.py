class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        ans = []
        while left < right and top < bottom:
            for idx in range(left, right+1):
                ans.append(matrix[top][idx])
            for idx in range(top+1, bottom):
                ans.append(matrix[idx][right])
            for idx in range(right, left-1, -1):
                ans.append(matrix[bottom][idx])
            for idx in range(bottom-1, top, -1):
                ans.append(matrix[idx][left])
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        if left == right:
            for idx in range(top, bottom+1):
                ans.append(matrix[idx][left])
        elif top == bottom:
            for idx in range(left, right+1):
                ans.append(matrix[top][idx])
        return ans


'''
维护记录边界的数据逐渐缩圈即可
时间复杂度：O(mn)
空间复杂度：O(1)
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = 0
        while left < right :
            res = max(res, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right] :
                left += 1
            else :
                right -= 1
        return res
'''
解析：
使用双指针left，right记录左右边界
考虑h的更小值缩减（不可能再以此为边界）
'''

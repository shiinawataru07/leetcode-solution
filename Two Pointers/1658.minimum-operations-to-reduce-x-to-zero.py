class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        left, right = 0, 1
        val = nums[0]
        n = len(nums)
        if target == 0:
            return n
        best_len, best_left, best_right = -1, -1, -1
        while True:
            if val < target:
                if right < n:
                    val += nums[right]
                    right += 1
                else:
                    break
            elif val == target:
                if right - left > best_len:
                    best_len = right - left
                    best_left = left
                    best_right = right
                val -= nums[left]
                left += 1
            else:
                val -= nums[left]
                left += 1
        nums = nums[best_left: best_right]
        return -1 if best_len == -1 else n - best_len

'''
求出最小操作数等价于求出最长子数组使得子数组和等于 sum(nums)-x
答案即为 n - best_len
使用双指针维护一个滑动的窗口并在窗口边缘移动时维护窗口内数组和即可
时间复杂度 O(n) 空间复杂度 O(1)
'''

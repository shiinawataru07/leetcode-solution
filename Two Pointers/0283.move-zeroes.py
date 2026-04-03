class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums) :
            if nums[right] != 0 :
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
          
'''
解析：
left指针代表已处理完毕的序列的最右侧的右一位，如果是0则停滞不前
right指针代表处理的位置走向哪里
'''

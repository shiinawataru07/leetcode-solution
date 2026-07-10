class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        cpy = [num for num in nums]
        k %= n
        for idx in range(n):
            if idx < k:
                nums[idx] = cpy[idx - k + n]
            else:
                nums[idx] = cpy[idx - k]



'''
使用额外的数组来将每个元素放至正确的位置。
空间复杂度o(n)

可以使用环状替换或者数组翻转来进行优化，使得空间复杂度为o(1)
这里写出数组翻转的方法作为参考：
我们先将k%=n
只需先对整个数组进行翻转
然后对前k的子数组与后n-k的子数组分别翻转即可
'''

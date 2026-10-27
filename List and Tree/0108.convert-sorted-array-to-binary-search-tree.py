# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        if not nums: return None
        n = len(nums)
        root = TreeNode(nums[n // 2])
        root.left = self.sortedArrayToBST(nums[: n // 2])
        root.right = self.sortedArrayToBST(nums[n // 2 + 1:])
        return root

'''
选择节点的中间元素作为根节点，左子树为左半部分数组构成的二叉搜索树，右子树为右半部分数组构成的二叉搜索树。递归实现。
'''

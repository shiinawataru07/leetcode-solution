# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None :
            return []
        else :
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

'''
解析：
二叉树的中序遍历，通过递归搜索即可
左-中-右
'''

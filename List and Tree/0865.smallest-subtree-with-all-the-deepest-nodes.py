# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = None
        max_depth = 0
        def postorder(root: TreeNode | None, depth: int) -> int:
            nonlocal ans, max_depth
            if not root: return depth
            left_depth = postorder(root.left, depth + 1)
            right_depth = postorder(root.right, depth + 1)
            if left_depth == right_depth and left_depth >= max_depth:
                max_depth = left_depth
                ans = root
            return max(left_depth, right_depth)
        postorder(root, 0)
        return ans

'''
使用后序遍历，计算每个节点的左右子树的最大深度，如果左右子树的最大深度相等且大于当前记录的最大深度，则更新答案为该节点。
'''

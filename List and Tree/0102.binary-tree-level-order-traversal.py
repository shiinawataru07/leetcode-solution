# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if not root: return []
        q = deque([(root, 1)])
        res = []
        while q:
            cur, depth = q.popleft()
            if depth > len(res):
                res.append([])
            res[depth - 1].append(cur.val)
            if cur.left: q.append((cur.left, depth + 1))
            if cur.right: q.append((cur.right, depth + 1))
        return res

'''
使用队列进行广度优先搜索，记录每个节点的深度，将节点值按深度存入结果列表中。
'''

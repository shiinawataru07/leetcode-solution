# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return "null"
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        lst = iter(data.split(","))
        def build():
            val = next(lst)
            if val == "null": return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


'''
使用 dfs 递归实现序列化和反序列化，序列化时将节点值按前序遍历顺序存入字符串中，空节点用 "null" 表示；
反序列化时根据字符串构建二叉树，如果是 null 则返回 None，否则创建节点并递归构建左右子树。
'''

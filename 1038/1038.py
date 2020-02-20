# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.res = 0
        def dfs(root):
            if not root: return
            dfs(root.right)
            root.val = self.res = root.val + self.res
            dfs(root.left)
            return root
        return dfs(root)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return
            if root.left and (not root.left.left and not root.left.right):
                res += root.left.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

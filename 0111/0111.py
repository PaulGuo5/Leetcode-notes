# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = float("inf")
        def dfs(root, depth):
            nonlocal res
            if not root:
                return 
            if not root.left and not root.right:
                res = min(res, depth)       
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        dfs(root, 1) 
        return  res

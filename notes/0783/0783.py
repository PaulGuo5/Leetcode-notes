# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.res = float("inf")
        def dfs(root, lo, hi):
            if not root:
                return
            if root.left:
                self.res = min(self.res, root.val - root.left.val, root.left.val - lo)
            if root.right:
                self.res = min(self.res, root.right.val - root.val, hi - root.right.val)
            dfs(root.left, lo, root.val)
            dfs(root.right, root.val, hi)
        dfs(root, -float("inf"), float("inf"))
        return self.res
            
        

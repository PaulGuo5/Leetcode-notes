# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equal(s, t):
            if not s and not t: return True
            if not s or not t: return False
            return s.val == t.val and equal(s.left, t.left) and equal(s.right, t.right)
        
        def dfs(s, t):
            if not s: return False
            return equal(s, t) or dfs(s.left, t) or dfs(s.right, t)
        
        return dfs(s,t)

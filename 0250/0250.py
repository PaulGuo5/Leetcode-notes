# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root: return 0
        self.cnt = 0
        self.dfs(root, root.val)
        return self.cnt
        
    def dfs(self, root, pre_val):
        if not root: return True
        left = self.dfs(root.left, root.val)
        right = self.dfs(root.right, root.val)
        if left and right:
            self.cnt += 1
            if root.val == pre_val:
                return True
        return False

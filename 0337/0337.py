# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return 0, 0
            left, right = dfs(node.left), dfs(node.right)
            now = node.val + left[1] + right[1]
            later = max(left) + max(right)
            return now, later
        
        return max(dfs(root))

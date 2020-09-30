# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = left + 1 if node.left and node.left.val == node.val + 1 else 1
            right = right + 1 if node.right and node.right.val == node.val + 1 else 1
            self.res = max(self.res, max(left,right))
            return max(left, right)
        dfs(root)
        return self.res

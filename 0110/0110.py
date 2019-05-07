# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, root, depth):
            if not root:
                return depth
            elif not root.left and not root.right:
                return depth + 1
            return max(self.dfs(root.left, depth + 1),self.dfs(root.right, depth + 1))
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.dfs(root.left, 0)-self.dfs(root.right, 0)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return True
            if root.left and root.left.val != root.val:
                return False
            if root.right and root.right.val != root.val:
                return False
            else:
                return dfs(root.left) and dfs(root.right)
        return dfs(root)

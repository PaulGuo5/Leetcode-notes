# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, parent, depth, target):
            if not node:
                return
            if node.val == target:
                return parent, depth
            return dfs(node.left, node, depth+1, target) or dfs(node.right, node, depth+1, target)
        xp, xd = dfs(root, None, 0, x)
        yp, yd = dfs(root, None, 0, y)
        return xd == yd and xp != yp

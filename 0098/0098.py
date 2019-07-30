# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lo = -float('inf'), hi = float('inf')):
            if not root:
                return True
            if not lo < root.val < hi:
                return False
            return helper(root.left, lo, min(root.val, hi)) and helper(root.right, max(lo, root.val), hi)
        return helper(root)

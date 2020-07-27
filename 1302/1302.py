# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deepest = 0
        def deeps(root, deep):
            nonlocal deepest
            if not root:
                deepest = max(deepest, deep)
                return
            deeps(root.left, deep+1)
            deeps(root.right, deep+1)
        
        deeps(root, 0)
        cum = 0
        def helper(root, deep):
            nonlocal cum
            if not root:
                return
            if not root.left and not root.right and deep == deepest:
                cum += root.val
            helper(root.left, deep+1)
            helper(root.right, deep+1)
        helper(root, 1)
        return cum

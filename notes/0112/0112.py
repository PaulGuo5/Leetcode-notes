# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        res = False
        def helper(node, cur):
            nonlocal res
            if not node:
                return 
            cur += node.val
            if not node.left and not node.right:
                res = True if cur == sum else res
            
            helper(node.left, cur)
            helper(node.right, cur)
        
        helper(root, 0)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root
        def helper(root):
            if not root:
                return 
            
            if not root.left and root.val > val:
                root.left = TreeNode(val)
            elif not root.right and root.val < val:
                root.right = TreeNode(val)
            
            if root.val < val:
                helper(root.right)
            else:
                helper(root.left)
            return root
        return helper(root)

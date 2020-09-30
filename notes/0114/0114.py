# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return 
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        if l:
            root.right = l
            while l and l.right:
                l = l.right
            l.right = r
            root.left = None
        return root

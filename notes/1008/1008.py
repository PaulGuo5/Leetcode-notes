# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return []
        root = TreeNode(preorder.pop(0))
        def helper(root, val):
            if not root:
                return 
            if not root.left and val < root.val:
                root.left = TreeNode(val)
            elif not root.right and val > root.val:
                root.right = TreeNode(val)
            if root.val < val:
                helper(root.right, val)
            else:
                helper(root.left,val)
            return root
        while preorder:
            helper(root, preorder.pop(0))
        return root

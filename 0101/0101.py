# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def compareTree(self, left: TreeNode, right: TreeNode):
        if not left or not right:
            return left == right
        elif left.val == right.val:
            return self.compareTree(left.left,right.right) and self.compareTree(left.right,right.left) 
        elif left.val != right.val:
            return False
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compareTree(root.left, root.right)

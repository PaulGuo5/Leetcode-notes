# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 543. Diameter of Binary Tree
        self.res = 0
        def helper(root):
            if not root:
                return 0
            left_, right_ = helper(root.left), helper(root.right)
            left = left_+1 if root.left and root.left.val == root.val else 0
            right = right_+1 if root.right and root.right.val == root.val else 0
            self.res = max(self.res, left+right)
            return max(left, right)
        helper(root)
        return self.res

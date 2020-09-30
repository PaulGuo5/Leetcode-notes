# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        count = 0
        def sum_(root):
            nonlocal count
            if not root:
                return 0
            left, right = sum_(root.left), sum_(root.right)
            count += abs(left-right)
            return root.val + left + right
        sum_(root)
        return count
    def findTilt2(self, root: TreeNode) -> int:
        sum_ = 0
        def findT(root):
            nonlocal sum_
            if not root:
                return 0
            left = findT(root.left)
            right = findT(root.right)
            sum_ += abs(left-right)
            return root.val + left + right
        findT(root)
        return sum_

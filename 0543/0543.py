# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        tmp_path = 0
        def findMaxPath(root):
            nonlocal tmp_path
            if not root:
                return 0
            left = findMaxPath(root.left)
            right = findMaxPath(root.right)
            tmp_path = max(tmp_path, left + right)
            return max(left, right) + 1
        findMaxPath(root)
        return tmp_pathø


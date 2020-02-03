# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        self.l, self.r, self.x = 0, 0, x
        self.helper(root)
        p = n - (1 + self.l + self.r)
        return max(p, self.l, self.r) > n // 2
    
    def helper(self, root):
            if not root: return 0
            left = self.helper(root.left)
            right = self.helper(root.right)
            if root.val == self.x:
                self.l, self.r = left, right
            return 1 + left + right

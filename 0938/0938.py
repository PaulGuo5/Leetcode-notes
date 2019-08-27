# Definition for a binary tree node. class TreeNode:
#     def __init__(self, x):
#         self.val = x self.left = None self.right = None
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.sum = 0
        def dfs(root):
            if not root:
                return
            if L <= root.val <= R:
                self.sum += root.val
            dfs(root.left)
            dfs(root.right)
            return self.sum
        return dfs(root)
                

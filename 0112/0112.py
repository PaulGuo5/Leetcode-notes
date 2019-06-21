# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(root, sum_, sum):
            if not root:
                return False
            sum_ += root.val
            if not root.left and not root.right:
                return sum_ == sum
            return dfs(root.left, sum_, sum) or dfs(root.right, sum_, sum)
        return dfs(root, 0, sum)
        
            

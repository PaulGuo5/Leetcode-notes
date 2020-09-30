# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(root):
            if not root:
                return 
            root.left = dfs(root.left) 
            root.right = dfs(root.right)
            if root.val == target and root.left == root.right:
                return None
            return root
        
        return dfs(root)

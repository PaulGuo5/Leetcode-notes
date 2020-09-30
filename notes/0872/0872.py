# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root, leaves):
            if not root:
                return
            if not root.left and not root.right:
                leaves.append(root.val)
            dfs(root.left, leaves)
            dfs(root.right, leaves)
            return leaves
        return dfs(root1, []) == dfs(root2, [])

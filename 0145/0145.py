# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            dfs(root.right, res)
            res.append(root.val)
            return res
        return dfs(root, [])

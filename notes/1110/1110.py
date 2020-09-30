# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        res = []
        def dfs(root):
            if not root: return None
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if root.val not in to_delete: return root
            if root.left: res.append(root.left)
            if root.right: res.append(root.right)
            return None
        root = dfs(root)
        if root: res.append(root)
        return res

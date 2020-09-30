# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.b = []
        def dfs(root, path):
            if not root:
                return 
            path += str(root.val)
            if not root.left and not root.right:
                self.b.append(path)
                path = ""
            dfs(root.left, path)
            dfs(root.right, path)
        dfs(root, "")
        return sum([int(str(i), 2) for i in self.b])

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        def dfs(root, tmp_path, res_paths):
            if not root:
                return
            if not root.left and not root.right:
                tmp_path += str(root.val)
                res_paths.append(tmp_path)
            else:
                tmp_path += str(root.val) + "->"
                dfs(root.left, tmp_path, res_paths)
                dfs(root.right, tmp_path, res_paths)
            return res_paths
        return dfs(root, "", [])

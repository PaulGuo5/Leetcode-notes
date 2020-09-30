# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers1(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(root, cur):
            if not root:
                return
            cur = cur*10 + root.val
            if not root.left and not root.right:
                self.sum += cur
                return
            dfs(root.left, cur)
            dfs(root.right, cur)
                
        dfs(root, 0)
        return self.sum
    
    def sumNumbers(self, root: TreeNode) -> int:
        self.sum = 0
        def dfs(root, path):
            if not root:
                return
            path = path + [str(root.val)]
            if not root.left and not root.right:
                self.sum += int("".join(path))
                return
            dfs(root.left, path)
            dfs(root.right, path)
                
        dfs(root, [])
        return self.sum

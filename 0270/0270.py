# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue1(self, root: TreeNode, target: float) -> int:
        min_diff = float('inf')
        res = -1
        def dfs(root):
            nonlocal min_diff
            nonlocal res
            if not root: 
                return
            tmp = abs(root.val-target)
            if tmp < min_diff:
                min_diff = tmp
                res = root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
    
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = []
        min_diff = float('inf')
        while stack or root:
            while root:
                if min_diff > abs(root.val-target):
                    min_diff = abs(root.val-target)
                    res = root.val
                stack.append(root)
                if root.val < target:
                    break
                else:
                    root = root.left
            root = stack.pop()
            root = root.right
            
        return res

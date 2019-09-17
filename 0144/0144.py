# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def dfs(root, res):
            if not root:
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
            return res
        return dfs(root, [])
    
    
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res, stack = [], []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            node = stack.pop()
            node = node.right
        return res
        

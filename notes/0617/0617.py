# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(root1, root2):
            if not root1 and not root2:
                return
            elif not root1 and root2:
                return root2
            elif root1 and not root2:
                return root1
            elif root1 and root2:
                root1.val += root2.val
            
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            return root1
        return dfs(t1,t2)
    
    
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(root1, root2):
            if root1 and root2:
                root1.val += root2.val
            elif not root1:
                return root2
            elif not root2:
                return root1
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            return root1
        return dfs(t1,t2)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor1(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.nodes = []
        
        def helper(root):
            if not root: return
            helper(root.left)
            self.nodes.append(root)
            helper(root.right)
        
        helper(root)
        flag = False
        for n in self.nodes:
            if flag:
                return n
            if n == p:
                flag = True
        return None
    
    
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

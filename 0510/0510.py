"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        root = node
        while root.parent:
            root = root.parent
            
#         nodes = []
        
#         def dfs(node):
#             nonlocal nodes
#             if not node:
#                 return
#             dfs(node.left)
#             nodes.append(node)
#             dfs(node.right)
            
#         dfs(root)
#         flag = False
#         for n in nodes:
#             if flag:
#                 return n
#             if n == node:
#                 flag = True
        res = None
        while root:
            if root.val > node.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res

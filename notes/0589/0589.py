"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        nodes = []
        def helper(root, nodes):
            if not root:
                return
            nodes.append(root.val)
            for child in root.children:
                helper(child, nodes)
        helper(root, nodes)
        return nodes

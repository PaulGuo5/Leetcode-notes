"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def helper(root, nodes):
            if not root:
                return
            for child in root.children:
                helper(child, nodes)
            nodes.append(root.val)
        nodes = []
        helper(root, nodes)
        return nodes

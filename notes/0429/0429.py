"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res, queue = [], [root] if root else []
        while queue:
            res.append([node.val for node in queue])
            queue = [child for node in queue for child in node.children]
        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        level, queue = 0, [root] if root else []
        while queue:
            level += 1
            queue = [child for node in queue for child in node.children]
        return level

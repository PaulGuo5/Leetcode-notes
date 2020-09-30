"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque, defaultdict
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        table = defaultdict(list)
        level = 0
        queue = deque([(level, root)])
        while queue:
            level, node = queue.popleft()
            table[level].append(node)
            if node.left:
                queue.append((level+1, node.left))
            if node.right:
                queue.append((level+1, node.right))
        for index, node in table.items():
            for i in range(len(node)-1):
                node[i].next = node[i+1]
        return root

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        table = {}
        cur = head
        while cur:
            table[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            table[cur].next = table.get(cur.next, None)
            table[cur].random = table.get(cur.random, None)
            cur = cur.next
        return table[head]

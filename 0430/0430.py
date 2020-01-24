"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        dummy = Node(None, None, head, None)
        self.dfs(dummy, head)
        dummy.next.prev = None
        return dummy.next
    def dfs(self, pre, cur):
        if not cur: return pre
        cur.prev = pre
        pre.next = cur
        tmpNext = cur.next
        tail = self.dfs(cur, cur.child)
        cur.child = None
        return self.dfs(tail, tmpNext)

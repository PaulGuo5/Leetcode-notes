"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            newNode = Node(insertVal)
            newNode.next = newNode
            return newNode
        pre, cur = head, head.next
        insertedFlag = 0
        while True:
            if pre.val <= insertVal <= cur.val:
                insertedFlag = 1
            elif pre.val > cur.val:
                if insertVal >= pre.val or insertVal <= cur.val:
                    insertedFlag = 1
            if insertedFlag:
                pre.next = Node(insertVal, cur)
                return head
            pre, cur = cur, cur.next
            if head == pre:
                break
        pre.next = Node(insertVal, cur)
        return head

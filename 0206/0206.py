# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return[]
        tail = head
        curr = head.next
        while curr:
            head.next = curr.next
            curr.next = tail
            tail = curr
            curr = head.next
        return tail

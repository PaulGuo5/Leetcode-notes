# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less = less_head = ListNode(0)
        larger = larger_head = ListNode(0)
        while head:
            if head.val < x:
                less.next = ListNode(head.val)
                less = less.next
            else:
                larger.next = ListNode(head.val)
                larger = larger.next
            head = head.next
        less.next = larger_head.next
        return less_head.next

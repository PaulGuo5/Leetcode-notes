# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        d_odd = odd = ListNode(0)
        d_even = even = ListNode(0)
        while head:
            odd.next = head
            odd = odd.next
            even.next = head.next
            even = even.next
            if even:
                head = head.next.next
            else:
                head = None
        odd.next = d_even.next
        return d_odd.next

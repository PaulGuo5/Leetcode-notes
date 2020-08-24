# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # Iterative
        dummy = ListNode(0)
        cur = dummy
        dummy.next = head
        while head and head.next:
            tmp = head.next
            head.next = tmp.next
            tmp.next = head
            head = head.next
            cur.next = tmp
            cur = tmp.next
        return dummy.next
    
    def swapPairs1(self, head: ListNode) -> ListNode:
        # Recursive
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head

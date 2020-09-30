# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        while start.next:
            end = start
            for i in range(k-1):
                end = end.next
                if end.next == None: return dummy.next
            (start.next, start) = self.reverseList(start.next, end.next)
        return dummy.next
    
    def reverseList(self, start, end):
        dummy = ListNode(0)
        dummy.next = start
        while dummy.next != end:
            tmp = start.next
            start.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
        return (end, start)

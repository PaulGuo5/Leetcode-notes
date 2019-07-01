# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = p = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            next_val = cur.next.val
            if cur.val < next_val:
                cur = cur.next
                continue
            if p.next.val > next_val:
                p = dummy
            while p.next.val < next_val:
                p = p.next
            p.next, cur.next.next, cur.next =cur.next, p.next, cur.next.next
            # new = cur.next
            # cur.next = new.next
            # new.next = p.next
            # p.next = new
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        c1, c2 = "", ""
        while l1:
            c1 += str(l1.val)
            l1 = l1.next
        while l2:
            c2 += str(l2.val)
            l2 =l2.next
        sum_ = int(c1) + int(c2)
        dummy = ListNode(0)
        cur = dummy
        for i in str(sum_):
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next

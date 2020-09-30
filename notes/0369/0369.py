# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def plusOne1(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        digits = []
        while head:
            digits.append(str(head.val))
            head = head.next
        for i in str(int("".join(digits))+1):
            cur.next = ListNode(int(i))
            cur = cur.next
        return dummy.next
    
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next
        not_nine.val += 1
        nine = not_nine.next
        while nine:
            nine.val = 0
            nine = nine.next
        return dummy if dummy.val else dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def getLen(l):
            len_ = 0
            while l:
                len_ += 1
                l = l.next
            return len_
        
        def helper(l1, l2, diff):
            if not l1:
                return None
            if diff == 0:
                cur = ListNode(l1.val+l2.val)
            else:
                cur = ListNode(l1.val)
            
            if diff == 0:
                carry = helper(l1.next, l2.next, diff)
            else:
                carry = helper(l1.next, l2, diff-1)
            
            if carry and carry.val//10 > 0:
                cur.val += 1
                carry.val %= 10
            cur.next = carry
            return cur
        
        len_1, len_2 = getLen(l1), getLen(l2)
        if len_1 < len_2:
            return self.addTwoNumbers(l2, l1)
        diff = len_1 - len_2
        dummy = ListNode(0)
        dummy.next = helper(l1, l2, diff)
        
        if dummy.next.val//10 > 0:
            dummy.next.val %= 10
            dummy.val += 1
            return dummy
        
        return dummy.next
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        tail = head
        curr = head.next
        while curr:
            head.next = curr.next
            curr.next = tail
            tail = curr
            curr = head.next
        return tail
    
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        curr = head
        vals = []
        while curr.next:
            vals.append(curr.val)
            curr = curr.next
        vals.append(curr.val)
        
        new_head = self.reverseList(head)
        i = 0
        while new_head:
            if new_head.val != vals[i]:
                return False
            new_head = new_head.next
            i += 1
        return True

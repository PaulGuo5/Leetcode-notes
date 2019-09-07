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
    
    def isPalindrome1(self, head: ListNode) -> bool:
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
    
    def isPalindrome2(self, head: ListNode) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return True if nums == nums[::-1] else False
    
    
    def isPalindrome(self, head):
        def reverse(head):
            dummy = ListNode(0)
            dummy.next = head
            tail = dummy
            while head and head.next:
                tmp = head.next
                head.next = tmp.next
                tmp.next = tail.next
                tail.next = tmp
            return dummy.next
        def reverse1(head):
            dummy = head
            cur = head.next
            while cur:
                head.next = cur.next
                cur.next = dummy
                dummy = cur
                cur = head.next
            return dummy
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        l1, l2 = [], []
        while cur.next:
            l1.append(cur.next.val)
            cur = cur.next
        n = reverse(head)
        while n:
            l2.append(n.val)
            n = n.next
        return True if l1 == l2 else False

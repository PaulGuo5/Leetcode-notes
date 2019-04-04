# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeList(self, l1, l2):
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            elif l1.val >= l2.val:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
    
    def sortList2(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        pre = slow.next
        slow.next = None
        return self.mergeList(self.sortList(head), self.sortList(slow))
    
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = fast = pre = head
        
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        pre.next = None
        return self.mergeList(self.sortList(head), self.sortList(slow))        

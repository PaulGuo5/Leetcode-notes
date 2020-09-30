# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
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
        
        if not head:
            return
        # ensure the first part has the same or one more node
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse the second half
        node = reverse(slow.next)
        slow.next = None
        
        # combine head part and node part
        p = head
        while node:
            tmp = node.next
            node.next = p.next
            p.next = node
            p = node.next
            node = tmp

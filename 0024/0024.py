# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = curr = ListNode(0)
        dummy.next = head
        while curr.next:
            temp = curr.next
            if not temp.next:
                break
            curr.next = curr.next.next
            temp.next = curr.next.next
            curr.next.next = temp
            curr = curr.next.next
        return dummy.next
    def swapPairs2(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head
        while curr.next:
            temp = curr.next
            if not temp.next:
                break
            curr.next = temp.next
            temp.next = curr.next.next
            curr.next.next = temp
            curr = curr.next.next
        return dummy.next

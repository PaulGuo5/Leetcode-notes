# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = dummy = ListNode(0)
        dummy.next = head
        while curr.next:
            temp = curr.next
            if not temp.next:
                break
            if temp.next.val == temp.val:
                curr.next = temp.next
            else:
                curr = curr.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = dummy = ListNode(0)
        dummy.next = head
        while cur:
            flag = 0
            while cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                flag = 1
                cur.next = cur.next.next
            if flag:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
        

    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = collections.Counter(nums)
        new = []
        for i, j in n.items():
            if j == 1:
                new.append(i)
        if not new:
            return
        dummy = ListNode(0)
        cur = ListNode(new[0])
        dummy.next = cur
        for i in new[1:]:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeZeroSumSublists1(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, dummy.next
        s = 0
        table = {s: pre}
        while cur:
            s += cur.val
            if s in table:
                table[s].next = cur.next
            else:
                table[s] = cur
            pre, cur = cur, cur.next
        return dummy.next
    
    def removeZeroSumSublists(self, head):
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = collections.OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next

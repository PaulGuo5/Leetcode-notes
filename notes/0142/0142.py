# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = slow = head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                res = head
                while res != fast:
                    res = res.next
                    fast = fast.next
                return res
        return None
    
    def detectCycle(self, head):
            visitedNode = set()
            dummy = head
            while dummy:
                if dummy in visitedNode:
                    return dummy
                visitedNode.add(dummy)
                dummy = dummy.next
            return None

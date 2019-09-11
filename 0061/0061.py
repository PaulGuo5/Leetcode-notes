# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight1(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        cur = head
        nodes = []
        while cur:
            nodes.append(cur.val)
            cur = cur.next
        m = len(nodes)   
        k = k % m
        nodes = nodes[-k:] + nodes[:m-k]
        dummy = ListNode(0)
        cur = dummy
        for i in nodes:
            if m > 0:
                m -= 1
                cur.next = ListNode(i)
                cur = cur.next
        return dummy.next
    
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or k == 0:
            return head
        fast = slow = head
        length = 1

        while k and fast.next:
            fast = fast.next
            length += 1
            k -= 1
            
        if k != 0:
            k = (k + length - 1) % length
            return self.rotateRight(head, k)
        else:
            while fast.next:
                fast = fast.next
                slow = slow.next
            fast.next = head
            head = slow.next
            slow.next = None
            return head

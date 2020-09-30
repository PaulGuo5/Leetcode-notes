# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween1(self, head: ListNode, m: int, n: int) -> ListNode:
        if n == m:
            return head
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy
        cnt_p = 0
        cnt = 0
        while head and head.next:
            cnt_p += 1
            if cnt_p == m:
                while head and head.next:
                    tmp = head.next
                    head.next = tmp.next
                    tmp.next = tail.next
                    tail.next = tmp
                    cnt+=1
                    if cnt == n-m:
                        break
            else:
                head = head.next
                tail = tail.next
        return dummy.next
    
    
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        position = 1
        while position < m and cur.next:
            position += 1
            cur = cur.next
        tail = cur
        head = cur.next
        while head and head.next and position < n:
            tmp = head.next
            head.next = tmp.next
            tmp.next = tail.next
            tail.next = tmp
            position += 1
        return dummy.next

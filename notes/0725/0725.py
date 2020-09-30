# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        len_, node = 0, root
        while node:
            len_ += 1
            node = node.next
        n, remain = divmod(len_, k)
        cur, pre = root, None
        res = []
        for _ in range(k):
            width = n + 1 if remain>0 else n
            remain -= 1
            res.append(cur)
            if cur:
                for _ in range(width):
                    pre = cur
                    cur = cur.next
                pre.next = None
        return res

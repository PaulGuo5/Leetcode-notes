# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        currA, currB = headA, headB
        countA, countB = 0, 0
        start = None
        while currA.next:
            currA = currA.next
            countA += 1
        while currB.next:
            currB = currB.next
            countB += 1
        currA, currB = headA, headB
        if countA > countB:
            diff = countA - countB
            while diff:
                currA = currA.next
                diff -= 1
        elif countA < countB:
            diff = countB - countA
            while diff:
                currB = currB.next
                diff -= 1
        while currA and currB:
            if currA is currB:
                if not start:
                    start = currA
            else:
                start = None
            currA = currA.next
            currB = currB.next
        return start


    def getIntersectionNode(self, headA, headB):
        ptA, ptB = headA, headB
        flag = 0 # l1+l2 or l2+l1
        while ptA and ptB:
            if ptA == ptB:
                return ptA
            ptA = ptA.next
            ptB = ptB.next
            if not ptA and not flag:
                ptA = headB
                flag = 1
            if not ptB:
                ptB = headA
        return None

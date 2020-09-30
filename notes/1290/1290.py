# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        res = 0
        nums = nums[::-1]
        for i in range(len(nums)):
            res += nums[i]*2**i
        return res

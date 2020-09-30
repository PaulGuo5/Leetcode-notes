class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        table = {}
        stack = []
        res = []
        for n in nums2[::-1]:
            while stack and stack[-1] < n:
                stack.pop()
            if stack:
                table[n] = stack[-1]
            else:
                table[n] = -1
            stack.append(n)
        for n in nums1:
            res.append(table[n])
        return res

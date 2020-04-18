class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = [(0, -1)]
        for i, h in enumerate(heights):
            while stack[-1][1] != -1 and stack[-1][0] >= h:
                res = max(res, stack.pop()[0]*(i-stack[-1][1]-1))
            stack.append((h, i))
        while stack[-1][1] != -1:
            res = max(res, stack.pop()[0]*(len(heights)-stack[-1][1]-1))
        return res

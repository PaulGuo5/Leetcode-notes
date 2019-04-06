# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        res = []
        stack = []
        points = []
        for interval in intervals:
            points.append([interval.start,0])
            points.append([interval.end,1])
        points.sort()
        
        for i, j in points:
            if not j:
                stack.append(i)
            else:
                start = stack.pop()
                if not stack:
                    res.append([start,i])
        return res

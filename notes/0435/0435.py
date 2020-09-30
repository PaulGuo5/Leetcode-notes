class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort()
        pre = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[pre][1]:
                res += 1
                if intervals[i][1] < intervals[pre][1]:
                    pre = i
            else:
                pre = i
        return res

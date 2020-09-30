class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_sorted = sorted([[start, end, idx] for idx, [start, end] in enumerate(intervals)])
        starts = [start for start, _, _ in intervals_sorted]
        res = [-1]*len(intervals)
        
        for start, end, idx in intervals_sorted:
            x = bisect.bisect_left(starts, end)
            if x < len(starts):
                res[idx] = intervals_sorted[x][2]
        return res
            

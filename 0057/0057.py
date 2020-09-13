class Solution:
    def insert1(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals):
            if newInterval[0] >= intervals[i][0]:
                i += 1
            else:
                break
        intervals.insert(i, newInterval)
        
        res = [intervals[0]]
        for i in intervals[1:]:
            if i[0] > res[-1][1]:
                res.append(i)
            else:
                pre = res.pop()
                new = [pre[0], max(pre[1], i[1])]
                res.append(new)
        return res
    
    
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, right = [], []
        s, e = newInterval[0], newInterval[1]
        for i in intervals:
            if i[1] < s:
                left += [i]
            elif i[0] > e:
                right += [i]
            else:
                s = min(s, i[0])
                e = max(e, i[1])
        return left+[[s, e]]+right

"""
# Definition for an Interval.
class  v:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def employeeFreeTime1(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        worktime = []
        for i in schedule:
            for j in i:
                worktime.append(j)
        worktime = sorted(worktime, key=lambda x: x.start)
        if not worktime: return []
        pre_end = worktime[0].end
        res = []
        for i in worktime:
            if i.start > pre_end:
                res.append(Interval(pre_end, i.start))
                pre_end = i.end
            if pre_end < i.end:
                pre_end = i.end
        return res
    
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        worktime = []
        for i in schedule:
            for j in i:
                worktime.append((j.start, 0))
                worktime.append((j.end, 1))
        worktime.sort()
        pre = None
        res = []
        bal = 0
        for i,j in worktime:
            if pre is not None and bal == 0:
                res.append(Interval(pre, i))
            bal += 1 if j == 0 else -1
            pre = i
        return res

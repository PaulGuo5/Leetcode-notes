class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ts = set()
        for t in timePoints:
            tmp = t.split(":")
            ts.add(int(tmp[0])*60+int(tmp[1]))
        if len(ts) < len(timePoints): return 0
        t = [0]*24*60
        for i in ts:
            t[i] = 1
        tt = t + t
        prev = -24*60
        res = 24*60
        for i in range(len(tt)):
            if tt[i] == 1:
                res = min(res, i-prev)
                prev = i
        return res

class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxlen = max([i[1] for i in clips])
        timeline = [0]*(maxlen+1)
        for clipstart, clipend in clips:
            timeline[clipstart] = max(timeline[clipstart], clipend)
            
        res = 0
        near, far = 0, 0
        for i, n in enumerate(timeline):
            if i > far or i > T: break
            if i > near:
                near = far
                res += 1
            far = max(far, n)
        return res if far >= T else -1

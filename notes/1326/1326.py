class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0]*(n+1)
        for i, dis in enumerate(ranges):
            left, right = max(0, i-dis), min(n, i+dis)
            max_range[left] = max(max_range[left], right - left)
        
        far, near = 0, 0
        res = 0
        for i, dis in enumerate(max_range):
            if i > far: return -1
            if i > near:
                res += 1
                near = far
            far = max(far, dis+i)
        return res
                

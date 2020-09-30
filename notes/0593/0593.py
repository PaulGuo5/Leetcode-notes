class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(a, b):
            return (a[0]-b[0])**2+(a[1]-b[1])**2
        
        cnt = collections.Counter()
        for a, b in list(itertools.combinations([p1, p2, p3, p4], 2)):
            cnt[dist(a, b)] += 1
        if len(cnt) != 2: return False
        diag, side = max(cnt.keys()), min(cnt.keys())
        return diag == side * 2 and cnt[diag] == 2 and cnt[side] == 4

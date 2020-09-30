class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.presum = [0]*(len(self.rects)+1)
        for i in range(1, len(self.presum)):
            self.presum[i] = self.presum[i-1] + self.area(self.rects[i-1])
            
    def area(self, rect):
        x1, y1, x2, y2 = rect
        return (x2-x1+1)*(y2-y1+1)

    def pick(self) -> List[int]:
        n = random.randint(1, self.presum[-1])
        i = bisect.bisect_left(self.presum, n)
        n -= self.presum[i-1]
        x1, y1, x2, y2 = self.rects[i-1]
        q, r = divmod(n, x2-x1+1)
        if r:
            return [(x1+r)-1, (y1+q+1)-1]
        else:
            return [x2, (y1+q)-1]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()

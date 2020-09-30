class Solution:
    def numPairsDivisibleBy601(self, time: List[int]) -> int:
        # exceed time limit
        res = 0
        for i,j in itertools.combinations(time, 2):
            if (i+j) % 60 == 0:
                res += 1
        return res
    
    
    def numPairsDivisibleBy602(self, time: List[int]) -> int:
        c = collections.Counter()
        res = 0
        for t in time:
            res += c[-t % 60]
            c[t % 60] += 1
        return res

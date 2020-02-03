class Solution:
    def stoneGame1(self, piles: List[int]) -> bool:
        # Time:O(2^n) Space:O(n)
        def helper(piles, l, r):
            if l > r: return 0
            if l == r: return piles[l]
            return max(piles[l]-helper(piles, l+1, r),
                      piles[r]-helper(piles, l, r-1))
        return helper(piles, 0, len(piles)-1) > 0
    
    
    def stoneGame2(self, piles: List[int]) -> bool:
        # Time:O(n^2) Space:O(n^2)
        self.memo = [[float('inf')]*len(piles) for _ in range(len(piles))]
        def helper(piles, l, r):
            if l > r: return 0
            if l == r: return piles[l]
            if self.memo[l][r] != float('inf'):
                self.memo[l][r] = max(piles[l]-helper(piles, l+1, r), piles[r]-helper(piles, l, r-1))
            return self.memo[l][r]
        
        return helper(piles, 0, len(piles)-1) > 0
    
    
    def stoneGame(self, piles: List[int]) -> bool:
        # Time:O(n^2) Space:O(n^2)
        dp = [[0]*len(piles) for _ in range(len(piles))]
        for i in range(len(dp)):
            dp[i][i] = piles[i]
        for l in range(2, len(piles)+1):
            for i in range(len(piles)-l+1):
                j = i + l - 1
                dp[i][j] = max(piles[i]-dp[i+1][j], piles[j]-dp[i][j-1])
        return dp[0][-1]>0

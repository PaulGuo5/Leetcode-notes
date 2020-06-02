class Solution:
    def countSubstrings1(self, s: str) -> int:
        n = len(s)
        def helper(l, r):
            res = 0
            while 0<=l<n and 0<=r<n and s[l] == s[r]:
                res +=1
                l -= 1
                r += 1
            return res
        
        res = 0
        for i in range(n):
            res += helper(i, i)+helper(i, i+1)
        return res
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and ((j-i+1)<3 or dp[i+1][j-1])
                res += dp[i][j]
        return res

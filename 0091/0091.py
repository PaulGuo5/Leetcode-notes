class Solution:
    def numDecodings1(self, s: str) -> int:
        def canDoubleDigit(s):
            return len(s) == 2 and (s[0] == '1' or (s[0] == '2' and s[1] <= '6'))
        
        def helper(s):
            if s == '':
                return 1
            elif s[0] == '0':
                return 0

            flag = True if canDoubleDigit(s[:2]) else False

            if flag:
                return helper(s[1:]) +  helper(s[2:])
            else:
                return helper(s[1:])
            
        return helper(s)
    
    
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        l = len(s)
        dp = [0 for _ in range(l+1)]
        dp[0] = 1
        
        for i in range(1, l+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if len(s[i-2:i]) == 2 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
        
        return dp[-1]

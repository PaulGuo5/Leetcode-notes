class Solution:
    def longestPalindrome1(self, s: str) -> str:
        def getLen(s, l, r):
            if r >= len(s) or s[l] != s[r]:
                return 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return (r-1) - (l+1) + 1
        
        start, end = 0, 0
        for i in range(len(s)):
            if i + (end-start) // 2 > len(s):
                break
            l = max(getLen(s, i, i), getLen(s, i, i+1))
            if l > end - start:
                start = i - (l-1)//2
                end = start + l
        return s[start:end]
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        dp = [[0]*n for _ in range(n)]
        res_end, res_start = 0, 0
        maxLen = 0
        for i in range(n):
            dp[i][i] = 1
        for end in range(n):
            for start in range(i):
                dp[start][end] = (s[start] == s[end]) and (end-start<=2 or dp[start+1][end-1])
                if dp[start][end] and end-start+1 > maxLen:
                    maxLen = end-start+1
                    res_end, res_start = end, start
        return s[res_start:res_end+1] if maxLen > 0 else ""
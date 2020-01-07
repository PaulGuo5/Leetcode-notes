class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0]*(len(s)+1)
        dp[0] = 1
        words = set(wordDict)
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] == 1 and s[j:i] in words:
                    dp[i] = 1
        return dp[-1] == 1

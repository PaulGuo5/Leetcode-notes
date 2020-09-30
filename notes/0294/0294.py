class Solution:
    def canWin(self, s: str) -> bool:
        return self.helper(s, memo={})
    
    def helper(self, s, memo):
        if s in memo:
            return memo[s]
        for i in range(len(s)-1):
            if s[i] == s[i+1] == "+":
                tmp = s[:i] + "--" + s[i+2:]
                if not self.helper(tmp, memo):
                    memo[s] = True
                    return True
        memo[s] = False
        return memo[s]

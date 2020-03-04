class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        m, d = maxChoosableInteger, desiredTotal
        if m >= d: return True
        if m*(m+1)//2 < d: return False
        return self.helper([False]*m, {}, 0, d)
    
    def helper(self, state, memo, cur, target):
        if cur >= target:
            return False
        s = tuple(state)
        if s in memo:
            return memo[s]
        for i in range(len(state)):
            if not state[i]:
                state[i] = True
                if not self.helper(state, memo, cur+i+1, target):
                    memo[s] = True
                    state[i] = False
                    return memo[s]
                state[i] = False
        
        memo[s] = False
        return memo[s]
                

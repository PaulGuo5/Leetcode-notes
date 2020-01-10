class Solution:
    def minWindow(self, S: str, T: str) -> str:
        cur = [None]*len(S)
        for i in range(len(S)):
            if S[i] == T[0]:
                cur[i] = i
        for i in range(1, len(T)):
            new = [None]*len(S)
            last = None
            for j in range(len(cur)):
                if last is not None and T[i] == S[j]:
                    new[j] = last
                if cur[j] is not None:
                    last = cur[j]
            cur = new
        
        res = 0, len(S)
        for i in range(len(S)):
            if cur[i] is not None and i - cur[i] < res[1] - res[0]:
                res = cur[i], i
        return S[res[0]: res[1]+1] if res[1] < len(S) else ""

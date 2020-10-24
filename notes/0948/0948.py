class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        if not tokens or not P:
            return 0
        tokens.sort()
        q = collections.deque(tokens)
        res = tmp = 0
        while q and (q[0] <= P or tmp > 0):
            while q and q[0] <= P:
                P -= q.popleft()
                tmp += 1
            res = max(res, tmp)
            if q and tmp > 0:
                P += q.pop()
                tmp -= 1
        return res

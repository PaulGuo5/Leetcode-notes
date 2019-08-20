class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        q, r = divmod(len(B), len(A))
        if r != 0:
            q += 1
        if B in A*q:
            return q
        if B in A*(q+1):
            return q+1
        return -1

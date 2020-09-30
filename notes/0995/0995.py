class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = 0
        has_flipped = [0]*len(A)
        res = 0
        for idx, num in enumerate(A):
            if idx >= K:
                flipped ^= has_flipped[idx-K]
            if flipped ^ num == 0:
                if idx + K > len(A):
                    return -1
                flipped ^= 1
                has_flipped[idx] ^= 1
                res += 1
        return res

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMost(A, K) - self.atMost(A, K-1)
    def atMost(self, A, K):
        cnt = collections.Counter()
        i = res = 0
        for j in range(len(A)):
            if cnt[A[j]] == 0: K -= 1
            cnt[A[j]] += 1
            while K < 0:
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0: K += 1
                i += 1
            res += j - i + 1
        return res

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1] * n
        p_map = {}
        for p in primes:
            p_map[p] = 0
        for i in range(1, n):
            # min_ = 0xffffffff
            min_ = float('inf')
            for p in primes:
                if ugly[p_map[p]] * p < min_:
                    min_ = ugly[p_map[p]] * p
            ugly[i] = min_
            for p in primes:
                if min_ == ugly[p_map[p]] * p:
                    p_map[p] += 1
        return ugly[-1]

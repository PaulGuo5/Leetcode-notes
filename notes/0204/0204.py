class Solution:
    def isPrime(self, n):
        if n < 2:
            return 0
        if n == 2:
            return 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return 0
        return 1
    def countPrimes2(self, n: int) -> int:
        res = 0
        for i in range(2, n):
            res += self.isPrime(i)
        return res
    
    
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [1] * n
        primes[0] = primes[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                # primes[i * i: n: i] = [0] * len(primes[i * i: n: i])
                for j in range(i * i, n, i):
                    primes[j] = 0
        return sum(primes)

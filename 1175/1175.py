class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def fac(n):
            return 1 if n <= 1 else n * fac(n-1)
    
        def is_prime(a):
            if a == 1:return False
            for i in range(2, a):
                if a % i == 0:
                    return False
            return True
        
        def get_num_prime(n):
            return sum(is_prime(n) for n in range(1, n+1))
        
        m = get_num_prime(n)
        return fac(m) * fac(n-m) % (10**9 + 7)

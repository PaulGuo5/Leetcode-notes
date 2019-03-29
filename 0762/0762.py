class Solution:
    def isPrime(self, num):
        if num == 1:
            return False
        # for i in range(2,num):
        # for i in range(2,int(pow(num,0.5))+1):
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
        
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count_prime=0
        for i in range(L,R+1):
            count = 0
            primeNum = bin(i).count("1")
            if self.isPrime(primeNum):
                count_prime += 1
                #print(count_prime)
        return count_prime

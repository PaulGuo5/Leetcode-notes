class Solution:
    def subtractProductAndSum1(self, n: int) -> int:
        pro, sum = 1, 0
        for i in str(n):
            pro *= int(i)
            sum += int(i)
        return pro - sum

    
    def subtractProductAndSum(self, n: int) -> int:
        pro, sum = 1, 0
        while n > 0:
            i = n % 10
            pro *= i
            sum += i
            n //= 10
        return pro - sum

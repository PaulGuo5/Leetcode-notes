class Solution:
    def newNumber(self, n):
            sum_ = 0
            while n:
                n, remain = divmod(n, 10)
                sum_ += remain ** 2
            return sum_
                
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            new_n = self.newNumber(n)
            if new_n == 1:
                return True
            if new_n in visited:
                return False
            visited.add(new_n)
            n = new_n

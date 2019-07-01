class Solution:
    def isUgly1(self, num: int) -> bool:
        if num < 1:
            return False
        if num in (1, 2, 3, 5):
            return True
        q5, r5 = divmod(num, 5)
        if r5 == 0:
            return self.isUgly(q5)
        else:
            q3, r3 = divmod(num, 3)
            if r3 == 0:
                return self.isUgly(q3) 
            else:
                q2, r2 = divmod(num, 2)
                if r2 == 0:
                    return self.isUgly(q2)
                else:
                    return False
                
    def isUgly(self, num: int):
        while not num % 5 and num != 0:
            num /= 5
        while not num % 3 and num != 0:
            num /= 3
        while not num % 2 and num != 0:
            num /= 2
        if num != 1:
            return False
        return True
        
            

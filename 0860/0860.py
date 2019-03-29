class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10 and five:
                ten += 1
                five -= 1
            elif bill == 20 and ten and five:
                ten -= 1
                five -= 1
            elif bill == 20 and five >= 3:
                five -= 3
            else:
                return False
        return True
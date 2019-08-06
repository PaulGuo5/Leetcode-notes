class Solution:
    def addStrings1(self, num1: str, num2: str) -> str:
        return str(int(num1)+int(num2))
    
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1)[::-1], list(num2)[::-1]
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        res = ""
        for i in range(len(num2)):
            carry, r = divmod(int(num1[i]) + int(num2[i]) + carry, 10)
            res += str(r)
        if num1[len(num2):]:
            for i in range(len(num2), len(num1)):
                carry, r = divmod(int(num1[i])+carry, 10)
                res += str(r)
        if carry != 0:
            res += str(carry)
        return res[::-1]

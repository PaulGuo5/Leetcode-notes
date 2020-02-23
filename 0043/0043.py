class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        res = [0]*(l1+l2)
        pos = len(res)-1
        for i in range(l1-1, -1, -1):
            tmp = pos
            for j in range(l2-1, -1, -1):
                res[tmp] += int(num1[i])*int(num2[j])
                res[tmp-1] += res[tmp]//10
                res[tmp] %= 10
                tmp -= 1
            pos -= 1
        
        for i in range(len(res)):
            if res[i] != 0 or i == len(res)-1:
                return "".join(map(str, res[i:]))
        return ""

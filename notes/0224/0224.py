class Solution:
    def calculate(self, s: str) -> int:
        res, num, flag = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+" or c == "-":
                res += flag * num
                num = 0
                flag = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(flag)
                res = 0
                flag = 1
            elif c == ")":
                res += flag * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        
        res += flag * num
        return res

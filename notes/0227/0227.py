class Solution:
    def calculate(self, s: str) -> int:
        num, stack, sign = 0, [], '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            if (not s[i].isdigit() and s[i] != " ") or i == len(s)-1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)

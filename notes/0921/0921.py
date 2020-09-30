class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        res = 0
        for par in S:
            if not stack:
                stack.append(par)
                res += 1
            else:
                last = stack.pop()
                if last == "(" and par == ")":
                    res -= 1
                    continue
                else:
                    stack.append(last)
                    stack.append(par)
                    res += 1
        return res    

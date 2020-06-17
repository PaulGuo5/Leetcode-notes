class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        comp = set()
        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))
            elif c == ")":
                if not stack:
                    continue
                else:
                    tmp = stack.pop()
                    comp.add(tmp[1])
                    comp.add(i)
        res = "" 
        for i, c in enumerate(s):
            if c in ("(", ")") and i not in comp:
                continue
            res += c
        return res

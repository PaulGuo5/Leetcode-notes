class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ""
        flag = 0
        for s in S:
            if (s == "(" and flag > 0) or (s == ")" and flag > 1):
                res += s
            if s == '(':
                flag += 1
            else:
                flag += -1
        return res


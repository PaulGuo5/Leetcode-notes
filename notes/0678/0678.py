class Solution:
    def checkValidString(self, s: str) -> bool:
        s_stack = []
        o_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                o_stack.append(i)
            elif s[i] == "*":
                s_stack.append(i)
            else:
                if not o_stack and not s_stack:
                    return False
                if o_stack:
                    o_stack.pop()
                elif s_stack:
                    s_stack.pop()
        
        while s_stack and o_stack:
            if o_stack[-1] < s_stack[-1]:
                o_stack.pop()
                s_stack.pop()
            else:
                break
        return True if not o_stack else False

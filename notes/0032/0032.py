class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        stack = []
        res = 0
        pre = -1
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if not stack:
                    pre = i
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i-pre)
                    else:
                        res = max(res,i-stack[-1])
        return res
    
    
    def longestValidParentheses(self, s: str) -> int:
        open_, close_ = 0, 0
        res = 0
        for i in range(len(s)):
            if s[i] == "(":
                open_ += 1
            else:
                close_ += 1
            if close_ > open_:
                open_, close_ = 0, 0
            elif close_ == open_:
                res = max(res, 2*close_)
                
        open_, close_ = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                open_ += 1
            else:
                close_ += 1
            if open_ > close_:
                open_, close_ = 0, 0
            elif close_ == open_:
                res = max(res, 2*close_)
                
        return res

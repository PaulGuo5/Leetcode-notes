class Solution:
    def removeInvalidParentheses1(self, s: str) -> List[str]:
        def isValid(s):
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                if c == ")":
                    count -= 1
                if count  < 0:
                    return False
            return count == 0
                    
        
        def dfs(s, start, l, r, res):
            if l == 0 and r == 0:
                if isValid(s):
                    res.append(s)
                return
            for i in range(start, len(s)):
                if i != start and s[i] == s[i-1]:
                    continue
                if s[i] == "(" or s[i] == ")":
                    if r > 0 and s[i] == ")":
                        dfs(s[:i]+s[i+1:], i, l, r-1, res)
                    elif l > 0 and s[i] == "(":
                        dfs(s[:i]+s[i+1:], i, l-1, r, res)
        l, r = 0, 0
        res = []
        for c in s:
            l += (c == "(")
            if l == 0:
                r += (c == ")")
            else:
                l -= (c == ")")
        dfs(s, 0, l, r, res)
        
        return res
    
    
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(s):
            stack = []
            for c in s:
                if c == "(":
                    stack.append("(")
                elif c == ")":
                    if not stack or stack.pop() != "(":
                        return False
            if stack:
                return False
            return True
        
        def dfs(s, start, l, r, res):
            if l == r == 0:
                if isValid(s):
                    res.append(s)
                return
            
            for i in range(start, len(s)):
                if s[i] == "(" or s[i] == ")":
                    if r > 0 and s[i] == ")":
                        dfs(s[:i]+s[i+1:], i, l, r - 1, res)
                    elif l > 0 and s[i] == "(":
                        dfs(s[:i]+s[i+1:], i, l-1, r, res)
                        
        l, r = 0, 0
        res = []
        for c in s:
            if c == "(":
                l += 1
            elif c == ")" and l == 0:
                r += 1
            elif c == ")" and l != 0:
                l -= 1
        dfs(s, 0, l, r, res)
        return set(res)

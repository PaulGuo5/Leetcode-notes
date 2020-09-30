class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        memo = {}
        def helper(s):
            nonlocal memo
            if s.isdigit():
                return [int(s)]
            if s in memo:
                return memo[s]
            res = []
            for i in range(len(s)):
                if s[i] in "+-*":
                    left = helper(s[:i])
                    right = helper(s[i+1:])
                    for l in left:
                        for r in right:
                            if s[i] == "+":
                                res.append(l+r)
                            elif s[i] == "-":
                                res.append(l-r)
                            elif s[i] == "*":
                                res.append(l*r)
            memo[s] = res
            return res
        
        return helper(input)
            

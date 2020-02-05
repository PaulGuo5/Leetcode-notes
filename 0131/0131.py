import copy
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s: return s
        res = []
        self.helper(s, [], res)
        return res
        
    def helper(self, s, tmp, res):
        # if not s: res.append(copy.copy(tmp))
        if not s: res.append(tmp[:])
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                tmp.append(s[:i])
                self.helper(s[i:], tmp, res)
                tmp.pop()

class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for s in S:
            if res and s == res[-1]:
                res.pop()
            else:
                res.append(s)
        return "".join(res)

class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        res = []
        for i in range(len(s)-1):
            if s[i] == s[i+1] == "+":
                tmp = s[:i] + "--" + s[i+2:]
                if tmp not in set(res):
                    res.append(tmp)
        return res

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        S = S.lower()
        res = []
        for c in S:
            if not c.isalpha():
                if not res:
                    res.append(c)
                else:
                    for i in range(len(res)):
                        res[i] += c
            else:
                if not res:
                    res.append(c.upper())
                    res.append(c)
                else:
                    tmp = []
                    for i in range(len(res)):
                        tmp.append(res[i] + c.upper())
                        res[i] += c
                    res+=tmp
        return res

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        S += "*"
        res = []
        fst, lst = 0, 0
        pre = 0
        cnt = 1
        for i in range(1, len(S)):
            if S[pre] == S[i]:
                cnt += 1
                lst += 1
            else:
                if cnt >= 3:
                    res.append([fst, lst])
                fst, lst = i, i
                cnt = 1
            pre = i
        return res

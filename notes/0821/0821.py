class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        e_pos = []
        res = []
        for e in range(len(S)):
            if S[e] == C:
                e_pos.append(e)
        print(e_pos)
        for i in range(len(S)):
            if S[i] == C:
                res.append(0)
            else:
                distance = 10000
                for d in e_pos:
                    if abs(d-i) < distance:
                        distance = abs(d-i)
                res.append(distance)
        return res
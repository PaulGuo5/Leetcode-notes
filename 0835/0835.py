class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a, b = [], []
        dic = collections.defaultdict(int)
        res = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    a.append((i, j))
                if B[i][j] == 1:
                    b.append((i, j))
        for xa, ya in a:
            for xb, yb in b:
                tmp = (xa-xb, ya-yb)
                dic[tmp] += 1
                res = max(res, dic[tmp])
        return res

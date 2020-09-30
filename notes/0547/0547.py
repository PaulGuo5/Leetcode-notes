class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        vis = set()
        
        def dfs(i):
            if i not in vis:
                for j in range(n):
                    if M[i][j] == 1:
                        vis.add(i)
                        dfs(j)
        res = 0
        for i in range(n):
            if i not in vis:
                dfs(i)
                res += 1
        return res

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0
        m = len(M)
        visited = set()
        cnt = 0
        for i in range(m):
            if i not in visited:
                self.dfs(M, i, visited)
                visited.add(i)
                cnt += 1
        return cnt
    
    def dfs(self, M, i, visited):
        if i not in visited:
            for j in range(len(M[i])):
                if M[i][j] == 1:
                    visited.add(i)
                    self.dfs(M, j, visited)

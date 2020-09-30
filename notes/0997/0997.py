class Solution:
    def findJudge1(self, N: int, trust: List[List[int]]) -> int:
        indegree, outdegree = [0]*(N+1), [0]*(N+1)
        for i in trust:
            indegree[i[1]] += 1
            outdegree[i[0]] += 1
        for i in range(1, N+1):
            if indegree[i] == N-1 and outdegree[i] == 0:
                return i
        return -1
    
    def findJudge(self, N, trust):
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        print(count)
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

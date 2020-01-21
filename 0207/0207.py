class Solution:
    def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        for i, j in prerequisites:
            self.graph[j].append(i)
        v = [None] * numCourses # 1 == visiting; 2 == visited
        for i in range(numCourses):
            if self.dfs(i, v): return False
        return True
    
    def dfs(self, i, v):
        if v[i] == 1: return True
        if v[i] == 2: return False
        v[i] = 1
        for j in self.graph[i]:
            if self.dfs(j, v): return True
        v[i] = 2
        return False
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        indegree = [0]*numCourses
        for i, j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        bfs = [i for i in range(numCourses) if indegree[i] == 0]
        for i in bfs:
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    bfs.append(j)
        return len(bfs) == numCourses

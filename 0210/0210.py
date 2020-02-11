class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0]*numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i] += 1
        bfs = [n for n in range(numCourses) if indegree[n] == 0]
        for i in bfs:
            for j in graph[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    bfs.append(j)
        return bfs if len(bfs) == numCourses else None

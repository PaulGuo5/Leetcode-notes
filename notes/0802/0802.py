class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        table = collections.defaultdict(list)
        indegree = [0]*len(graph)
        for i, nodes in enumerate(graph):
            indegree[i] = len(nodes)
            for node in nodes:
                table[node].append(i)
        q = collections.deque()
        for i, j in enumerate(indegree):
            if j == 0:
                q.append(i)
        while q:
            node = q.popleft()
            for next_node in table[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    q.append(next_node)
        return [i for i, j in enumerate(indegree) if j == 0]


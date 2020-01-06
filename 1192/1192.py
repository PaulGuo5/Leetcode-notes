class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])
        
        dfn = [None for _ in range(n)]
        low = [None for _ in range(n)]
        
        self.cur = 0
        def dfs(node, parent):
            if dfn[node] is None:
                dfn[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for child in graph[node]:
                    if dfn[child] is None:
                        dfs(child, node)
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[dfn[node]])
                else:
                    l = min([low[i] for i in graph[node]]+[dfn[node]])
                low[node] = l
        dfs(0, None)
        
        res = []
        for v in connections:
            if low[v[0]] > dfn[v[1]] or low[v[1]] > dfn[v[0]]:
                res.append(v)
        return res

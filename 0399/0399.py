class Solution:    
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(x, y, visited):
            if x == y:
                return 1.0
            visited.add(x)
            for n in graph[x]:
                if n in visited:
                    continue
                visited.add(n)
                d = dfs(n, y, visited)
                if d > 0:
                    return d * graph[x][n]
            return - 1.0
        
        graph = collections.defaultdict(dict)
        for (x, y), v in zip(equations, values):
            graph[x][y] = v 
            graph[y][x] = 1.0 / v
        # res = []
        # for x, y in queries:
        #     if x not in graph and y not in graph:
        #         res.append(-1.0)
        #     else:
        #         res.append(dfs(x, y, set()))
        # return res
        return [dfs(x, y, set()) if x in graph and y in graph else -1.0 for x, y in queries]
        

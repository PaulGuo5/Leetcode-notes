class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        vis = set()
        
        def dfs(node, path):
            if node == n - 1:
                res.append(path+[node])
                return
            vis.add(node)
            for child in graph[node]:
                dfs(child, path+[node])
            vis.remove(node)
        
        dfs(0, [])
        return res

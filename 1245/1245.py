class Solution:
    def treeDiameter1(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        bfs = {(node, None) for node, neis in graph.items() if len(neis) == 1}
        move = 0
        while bfs:
            bfs = {(nei, node) for node, pre in bfs for nei in graph[node] if nei != pre}
            move += 1
        return max(move-1, 0)
    
    
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for n1, n2 in edges:
            graph[n1].add(n2)
            graph[n2].add(n1)
        max_diameter = 0
        
        def dfs(i, pre):
            nonlocal max_diameter
            d1 = d2 = 0
            for node in graph[i]:
                if node != pre:
                    d = dfs(node, i)
                    if d > d1:
                        d1, d2 = d, d1
                    elif d > d2:
                        d2 = d
            max_diameter = max(max_diameter, d1+d2)
            return d1+1
        
        dfs(0, None)
        return max_diameter

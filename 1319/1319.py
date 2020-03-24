class Solution:
    def makeConnected1(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        G = [set() for i in range(n)]
        for i, j in connections:
            G[i].add(j)
            G[j].add(i)
        seen = [0] * n

        def dfs(i):
            if seen[i]: return 0
            seen[i] = 1
            for j in G[i]: dfs(j)
            return 1
        
        s = 0
        for i in range(n):
            s += dfs(i)
        return s - 1
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # Union find
        self.id, self.count = [i for i in range(n)], n
        
        def union(a, b):
            def find(x):
                while self.id[x] != x:
                    x = self.id[x]
                return x
            
            fa, fb = find(a), find(b)
            if fa == fb: return
            self.id[fa] = fb
            self.count -= 1
            
        for a, b in connections:
            union(a, b)
        return self.count - 1 if len(connections) >= n-1 else -1

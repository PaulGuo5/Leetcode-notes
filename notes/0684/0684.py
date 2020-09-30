class Solution:
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        # Union find O(nlog*n) = O(n)
        def findRoot(x, tree):
            if tree[x] == -1: return x
            root = findRoot(tree[x], tree)
            tree[x] = root
            return root
        
        tree = [-1]*(len(edges)+1)
        for e in edges:
            a = findRoot(e[0], tree)
            b = findRoot(e[1], tree)
            if a == b:
                return e
            tree[a] = b
            
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # dfs O(n^2)
        def dfs(a, b):
            visited = set()
            stack = [a]
            while stack:
                node = stack.pop()
                if node == b:
                    return True
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            return False
        
        graph = collections.defaultdict(list)
        res = []
        for a,b in edges:
            if a in graph and b in graph:
                if dfs(a, b):
                    res = [a, b]
            graph[a].append(b)
            graph[b].append(a)

        return res

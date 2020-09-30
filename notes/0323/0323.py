class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = [i for i in range(n)]
        
        def find(n, nodes):
            if nodes[n] == n: return n
            return find(nodes[n], nodes)
        
        def union(n1, n2):
            a = find(n1, nodes)
            b = find(n2, nodes)
            if a == b:
                return False
            nodes[b] = a
            return True
        
        for n1, n2 in edges:
            if union(n1, n2):
                n -= 1
        
        return n

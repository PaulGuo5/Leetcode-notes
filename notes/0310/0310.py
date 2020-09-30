class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n: return None
        if n == 1: return [0]
        graph = collections.defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
        leaves = [i for i in graph if len(graph[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                node = graph[leaf].pop()
                graph[node].remove(leaf)
                if len(graph[node]) == 1:
                    new_leaves.append(node)
            leaves = new_leaves
        return leaves

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # bfs
        if not node:
            return node
        # dic = collections.defaultdict(Node)
        dic = {}
        q = collections.deque([node])
        while q:
            cur = q.popleft()
            # dic[cur].val = cur.val
            if cur not in dic:
                dic[cur] = Node(cur.val)
            for nei in cur.neighbors:
                if nei not in dic:
                    # dic[nei].val = nei.val
                    dic[nei] = Node(nei.val)
                    q.append(nei)
                    
                dic[cur].neighbors.append(dic[nei])
        
        return dic[node]

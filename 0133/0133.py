"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return 
        nodes = {}
        head = Node(node.val)
        nodes[node.val] = head
        q = collections.deque([node])
        
        while q:
            node = q.popleft()
            for child in node.neighbors:
                if child.val not in nodes:
                    new = Node(child.val)
                    nodes[child.val] = new
                    q.append(child)
                nodes[node.val].neighbors.append(nodes[child.val])
        return head

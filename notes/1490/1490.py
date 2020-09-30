"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree1(self, root: 'Node') -> 'Node':
        # bfs
        if not root:
            return root
        new = None
        q = collections.deque([(None, root)])
        while q:
            parent, cur = q.popleft()
            node = Node(cur.val)
            if not new:
                new = node
            if parent:
                parent.children.append(node)
            for child in cur.children:
                q.append((node, child))
        return new
    
    def cloneTree2(self, root: 'Node') -> 'Node':
        # bfs
        if not root:
            return root
        # dic = collections.defaultdict(Node)
        dic = {}
        q = collections.deque([root])
        while q:
            cur = q.popleft()
            # dic[cur].val = cur.val
            if cur not in dic:
                dic[cur] = Node(cur.val)
            for child in cur.children:
                if child not in dic:
                    # dic[child].val = child.val
                    dic[child] = Node(child.val)
                    q.append(child)
                dic[cur].children.append(dic[child])
        return dic[root]
    
    def cloneTree(self, root: 'Node') -> 'Node':
        # dfs
        if not root:
            return root
        return Node(root.val, [self.cloneTree(child) for child in root.children])

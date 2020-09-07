# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree1(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return root
        dic = collections.defaultdict(NodeCopy)
        q = deque([root])
        while q:
            node = q.popleft()
            dic[node].val = node.val
            if node.left:
                dic[node].left = dic[node.left]
                q.append(node.left)
            if node.right:
                dic[node].right = dic[node.right]
                q.append(node.right)
            if node.random:
                dic[node].random = dic[node.random]
        return dic[root]
    
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        if not root:
            return None
        vis = {}
        def dfs(root):
            nonlocal vis
            if not root:
                return None
            if root in vis:
                return vis[root]
            new = NodeCopy(root.val, None, None, None)
            vis[root] = new
            
            new.left = dfs(root.left)
            new.right = dfs(root.right)
            new.random = dfs(root.random)
            return new
        return dfs(root)

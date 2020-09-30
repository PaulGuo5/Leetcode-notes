# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK1(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def buildParentMap(node, parent, parentMap):
            if not node:
                return
            parentMap[node] = parent
            buildParentMap(node.left, node, parentMap)
            buildParentMap(node.right, node, parentMap)
            
        parentMap = {}
        buildParentMap(root, None, parentMap)
        
        res = []
        visited = set()
        
        def dfs(node, dis):
            if not node or node in visited:
                return
            visited.add(node)
            if K == dis:
                res.append(node.val)
            elif K >= dis:
                dfs(node.left, dis+1)
                dfs(node.right, dis+1)
                dfs(parentMap[node], dis+1)
            
        dfs(target, 0)
        return res
    
    
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def buildGraph(node, parent, graph):
            if not node:
                return
            if parent:
                graph[node].append(parent)
            if node.left:
                graph[node].append(node.left)
                buildGraph(node.left, node, graph)
            if node.right:
                graph[node].append(node.right)
                buildGraph(node.right, node, graph)
            
        graph = collections.defaultdict(list)
        buildGraph(root, None, graph)
        
        visited = set()
        res = []
        
        q = collections.deque()
        q.append((target, 0))
        
        while q:
            node, dis = q.popleft()
            if node in visited:
                continue
            visited.add(node)
            
            if dis == K:
                res.append(node.val)
            elif dis <= K:
                for child in graph[node]:
                    q.append((child, dis+1))
        return res
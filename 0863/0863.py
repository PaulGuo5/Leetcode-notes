# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
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

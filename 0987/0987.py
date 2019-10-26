# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        vals = collections.defaultdict(list)
        def dfs(root, x=0, y=0):
            if not root:
                return
            vals[x].append((y, root.val))
            dfs(root.left, x-1, y+1)
            dfs(root.right, x+1, y+1)
            
        dfs(root)
    
        return [list(map(lambda x: x[1], sorted(arr))) for x, arr in sorted(vals.items())]

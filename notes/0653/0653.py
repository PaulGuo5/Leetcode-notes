# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget1(self, root: TreeNode, k: int) -> bool:
        nodes_val = []
        def dfs(root, nodes_val):
            if not root:
                return
            dfs(root.left, nodes_val)
            nodes_val.append(root.val)
            dfs(root.right, nodes_val)
        dfs(root, nodes_val)
        nodes_set = set()
        for i in nodes_val:
            nodes_set.add(i)
        for i in nodes_set:
            nodes_set.remove(i)
            if k-i in nodes_set:
                return True
            nodes_set.add(i)
        return False
    
    def findTarget2(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        bfs = [root]
        s = set()
        for i in bfs:
            if k-i.val in s:
                return True
            s.add(i.val)
            if i.left:
                bfs.append(i.left)
            if i.right:
                bfs.append(i.right)
        return False
    
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        def helper(root, k):
            if not root:
                return False
            if k-root.val in s:
                return True
            s.add(root.val)
            return helper(root.left, k) or helper(root.right, k)
        return helper(root, k)

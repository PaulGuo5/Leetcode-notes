# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes1(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return
            self.res += 1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.res
    
    
    def countNodes(self, root: TreeNode) -> int:
        def getHeight(root):
            h = 0
            while root.left:
                h += 1
                root = root.left
            return h
        
        def getNode(idx, root, h):
            left, right = 0, 2**h-1
            for _ in range(h):
                mid = (left+right) // 2
                if mid >= idx:
                    root = root.left
                    right = mid
                else:
                    root = root.right
                    left = mid + 1
            return root is not None
        
        if not root:
            return 0
        h = getHeight(root)
        if h == 0:
            return 1
        left, right = 0, 2**h-1
        while left <= right:
            mid = (left+right)//2
            if getNode(mid, root, h):
                left = mid + 1
            else:
                right = mid - 1
        return 2**h-1 + left

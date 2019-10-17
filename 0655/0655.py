# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            return max(height(root.left)+1, height(root.right)+1)
        
        def fill(root, l, r, h):
            if not root:
                return
            mid = (l+r) // 2
            m[h][mid] = str(root.val)
            if root.left:
                fill(root.left, l, mid-1, h+1)
            if root.right:
                fill(root.right, mid+1, r, h+1)
        
        h = height(root)
        w = 2**h - 1
        m = [["" for _ in range(w)] for _ in range(h)]
        fill(root, 0, w-1, 0)
        return m

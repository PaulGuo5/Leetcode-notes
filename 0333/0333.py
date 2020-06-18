# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal res
            if not root:
                return -float('inf'), float('inf'), 0, True
            max_left, min_left, cnt_nodes_left, isBST_left = dfs(root.left)
            max_right, min_right, cnt_nodes_right, isBST_right = dfs(root.right)
            cnt_nodes = cnt_nodes_left+cnt_nodes_right+1
            
            isBST = False
            if max_left < root.val < min_right:
                isBST = isBST_left and isBST_right
            if isBST:
                res = max(res, cnt_nodes)
            return max(max_left, root.val, max_right), min(min_left, min_right, root.val), cnt_nodes, isBST
        
        res = 0
        dfs(root)
        return res

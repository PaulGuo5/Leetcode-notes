# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return 0, 0
            left_cum, left_cnt = dfs(node.left)
            right_cum, right_cnt = dfs(node.right)
            
            tmp_cum = left_cum+right_cum+node.val
            tmp_cnt = left_cnt+right_cnt+1
            res = max(res, (tmp_cum)/(tmp_cnt))
            
            return tmp_cum, tmp_cnt
        dfs(root)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        
        def helper(node, cur, path):
            if not node:
                return
            cur += node.val
            if not node.left and not node.right:
                if cur == sum:
                    res.append(path+[node.val])
            helper(node.left, cur, path+[node.val])
            helper(node.right, cur, path+[node.val])
        
        helper(root, 0, [])
        return res

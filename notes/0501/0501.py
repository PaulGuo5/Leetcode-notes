# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
        
    def findMode(self, root: TreeNode) -> List[int]:
        count = {}
        def dfs(TreeNode):
            if TreeNode:
                if TreeNode.val in count:
                    count[TreeNode.val] += 1
                else:
                    count[TreeNode.val] = 1
                dfs(TreeNode.left)
                dfs(TreeNode.right)
        dfs(root)
        max_ = 0
        res = []
        for key, value in count.items():
            if value > max_:
                max_ = value
        for key, value in count.items():
            if max_ == value:
                res.append(key)
        return res

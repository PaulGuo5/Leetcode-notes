# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 0
        min_ = float("inf")
        def helper(root, res):
            if not root:
                return
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)
            return res
        res = sorted(helper(root, []))
        for i, j in zip(res[1:],res):
            if abs(j-i) < min_:
                min_ = abs(j-i)
        return min_

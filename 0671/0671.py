# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        value = set()
        def dfs(root):
            nonlocal value
            if not root.left and not root.right:
                value.add(root.val)
                return
            else:
                value.add(root.left.val)
                value.add(root.right.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        min_ = min(value)
        print(value)
        value.remove(min_)
        if not value:
            return -1
        return min(value)

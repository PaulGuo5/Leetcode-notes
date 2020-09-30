# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        dic = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            level = max(left, right) + 1
            dic[level].append(root.val)
            return level
        dfs(root)
        return dic.values()

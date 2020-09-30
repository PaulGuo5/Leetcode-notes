# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def helper(i, j, l):
            if l <= 0: return None
            root = TreeNode(pre[i])
            if l == 1: return root
            k = j
            while pre[i+1] != post[k]: k += 1
            left_part = k - j + 1
            root.left = helper(i+1, j, left_part)
            root.right = helper(i+left_part+1, k+1, l-left_part-1)
            return root
        return helper(0, 0, len(pre))

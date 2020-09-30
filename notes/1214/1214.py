# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        def dfs(root, nums):
            if not root: return
            nums.append(root.val)
            dfs(root.left, nums)
            dfs(root.right, nums)
         
        nums1, nums2 = [], []
        dfs(root1, nums1)
        dfs(root2, nums2)
        
        for i in nums1:
            if target-i in set(nums2):
                return True
        return False

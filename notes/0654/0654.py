# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def helper(nums, l, r):
            if l > r: return
            if l == r: return TreeNode(nums[l])
            
            mx = -float("inf")
            for i in range(l, r+1):
                if mx < nums[i]:
                    mx = nums[i]
                    mx_id = i
            node = TreeNode(mx)
            left = helper(nums, l, mx_id-1)
            right = helper(nums, mx_id+1, r)
            node.left = left
            node.right = right
            return node
        
        return helper(nums, 0, len(nums)-1)

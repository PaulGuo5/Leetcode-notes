# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
        def find2swap(nums):
            n = len(nums)
            x = y = -1
            for i in range(n-1):
                if nums[i+1] < nums[i]:
                    y = nums[i+1]
                    if x == -1:
                        x = nums[i]
                    else:
                        break
            return x, y
        
        def recover(node, count):
            if not node:
                return 
            if node.val == x or node.val == y:
                node.val = y if node.val == x else x
                count -= 1
                if count == 0:
                    return 
            recover(node.left, count)
            recover(node.right, count)
        
        nums = inorder(root)
        x, y  = find2swap(nums)
        recover(root, 2)
        return root

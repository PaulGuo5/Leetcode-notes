# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        res = []
        while root1 or stack1 or root2 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left
            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                smallest = stack1.pop()
                res.append(smallest.val)
                root1 = smallest.right
            else:
                smallest = stack2.pop()
                res.append(smallest.val)
                root2 = smallest.right
        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return  
        def helper(left,right):
            if not left and not right:
                return 
            left.next = right       
            helper(left.left,left.right)
            helper(right.left,right.right)
            helper(left.right,right.left)
        
        helper(root.left,root.right)
        return root

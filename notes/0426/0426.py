"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.inorder_list.append(root)
            inorder(root.right)
        
        self.inorder_list = []
        inorder(root)
        
        n = len(self.inorder_list)
        
        if not self.inorder_list:
            return None
        for i in range(n):
                self.inorder_list[i].left = self.inorder_list[(i - 1) % n]
                self.inorder_list[i].right = self.inorder_list[(i + 1) % n]
        
        return self.inorder_list[0]

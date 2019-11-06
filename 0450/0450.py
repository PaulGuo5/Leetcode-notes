# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode1(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if not root.left and not root.right:
                return None
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            root.val = min_node.val
            root.right = self.deleteNode(root.right, min_node.val)
        return root
    
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            left = root.left
            right = root.right
            p = right
            while p.left:
                p = p.left
            p.left = left
            return right
        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST1(self, root: TreeNode) -> TreeNode:
        # not correct
        def left_rotation(x, p):
            p_left = p.left
            p.left = x
            x.right = p_left
            return p
        
        def right_rotation(x, p):
            p_right = p.right
            p.right = x
            x.left = p_right
            return p
        
        def getHeight(node):
            if not node:
                return 0
            if not node.right:
                return getHeight(node.left)+1
            if not node.left:
                return getHeight(node.right)+1
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        def rebuild(node):
            if not node:
                return node
            left_height, right_height = getHeight(node.left), getHeight(node.right)
            diff = left_height - right_height
            if abs(diff) <= 1:
                return node
            elif diff > 1:
                return rebuild(right_rotation(node, node.left))
            elif diff < -1:
                return rebuild(left_rotation(node, node.right))
        
        return rebuild(root)
    
    
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        
        def helper(nodes):
            if not nodes:
                return None
            mid = len(nodes)//2
            node = TreeNode(nodes[mid])
            node.left = helper(nodes[:mid])
            node.right = helper(nodes[mid+1:])
            return node
        
        inorder(root)
        return helper(nodes)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            dfs(root.right, res)
            res.append(root.val)
            return res
        return dfs(root, [])
    
    
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        if not root: return []
        def reverseTree(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            reverseTree(root.left)
            reverseTree(root.right)
            return root
        root = reverseTree(root)
        stack, res = [], []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res[::-1]
    
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], []
        last_visited = ''
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            cur = stack[-1]
            if not cur.right or cur.right == last_visited:
                item = stack.pop()
                res.append(item.val)
                last_visited = item
            elif cur.right:
                root = cur.right
        return res
                

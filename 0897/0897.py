# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        s1 = []
        def dfs(root):
            nonlocal s1
            if not root:
                return
            dfs(root.left)
            s1.append(root.val)
            dfs(root.right)
        def newTree(i, array):
            if i == len(array):
                return None
            node = TreeNode(array[i])
            node.right = newTree(i+1,array)
            return node
        dfs(root)
        return newTree(0, s1)

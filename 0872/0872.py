# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getLeaf(self, root: TreeNode, leaf: list):
        if not root.left and not root.right:
            leaf.append(root.val)
        elif root.left and not root.right:
            self.getLeaf(root.left, leaf)
        elif root.right and not root.left:
            self.getLeaf(root.right, leaf)
        elif root.left and root.right:
            self.getLeaf(root.left, leaf)
            self.getLeaf(root.right, leaf)
        return leaf
    def leafSimilar2(self, root1: TreeNode, root2: TreeNode) -> bool:
        if self.getLeaf(root1, []) == self.getLeaf(root2, []):
            return True
        else:
            return False
        

    def leafSimilar(self, root1, root2):
        def dfs(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            res = []
            res = dfs(root.left) + res
            res += dfs(root.right)
            return res
        
        lst1 = dfs(root1)
        lst2 = dfs(root2)
        return lst1 == lst2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def newTree(root, left, right):
            node = TreeNode(root)
            node.left = left
            node.right = right
            return node
        def gen(begin, end):
            res = []
            for i in range(begin, end+1):
                for left in gen(begin, i-1):
                    for right in gen(i+1, end):
                        res.append(newTree(i, left, right))
            return res if res else [None]
        return gen(1, n) if n > 0 else []

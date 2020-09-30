# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res, queue = [], [root] if root else []
        while queue:
            level_len = len(queue)
            level_nodes = []
            while level_len > 0:
                node = queue.pop(0)
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_len -= 1
            res.append(level_nodes)
        return res[::-1]

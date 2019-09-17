# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from collections import defaultdict
class Solution:
    def levelOrder1(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res, queue, level = [], [], []
        queue.append(root)
        queue.append(None)
        while queue:
            node = queue.pop(0)
            if node:
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            else:
                res.append(level)
                if queue:
                    queue.append(None)
                level = []
        return res
    
    
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        table = defaultdict(list)
        level = 0
        queue = deque([(root, level)])
        while queue:
            cur, level = queue.popleft()
            table[level].append(cur.val)
            if cur.left:
                queue.append((cur.left, level+1))
            if cur.right:
                queue.append((cur.right, level+1))   
        return [table[index] for index in range(len(table))]

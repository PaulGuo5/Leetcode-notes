# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return
        queue = [root]
        res = []
        while queue:
            cur_queue = []
            cur_sum = 0
            for node in queue:
                cur_sum += node.val
                if node.left:
                    cur_queue.append(node.left)
                if node.right:
                    cur_queue.append(node.right)
            res.append(cur_sum / len(queue))
            queue = cur_queue
        return res

        

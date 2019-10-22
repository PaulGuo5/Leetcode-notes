# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        queue = collections.deque()
        flag = 1
        queue.append(root)
        res = []
        while queue:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            if flag == 1:
                res.append(tmp)
                flag = 0
            else:
                res.append(tmp[::-1])
                flag = 1
        return res
                

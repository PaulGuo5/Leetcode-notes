# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return None
        q = collections.deque([(root, 0, 0)])
        nodes = []
        while q:
            node, level, idx = q.popleft()
            nodes.append((idx, node.val))
            if node.left:
                q.append((node.left, level+1, idx-1))
            if node.right:
                q.append((node.right, level+1, idx+1))
        nodes = sorted(nodes, key=lambda x: x[0])
        min_idx = min(nodes, key=lambda x:x[0])[0]
        max_idx = max(nodes, key=lambda x:x[0])[0]
        res = [[] for _ in range(max_idx-min_idx+1)]
        for idx, val in nodes:
            res[idx-min_idx].append(val)
        return res

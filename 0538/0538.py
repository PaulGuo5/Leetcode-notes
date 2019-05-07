# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        nodes = []
        def dfs(root, nodes):
            if not root:
                return
            dfs(root.left, nodes)
            nodes.append(root)
            dfs(root.right, nodes)
        dfs(root, nodes)
        # for key, value in enumerate(nodes):
        #     print(key, value.val)
        cum = 0
        for node in nodes[::-1]:
            node.val += cum
            cum = node.val
        return root

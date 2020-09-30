# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees1(self, root: TreeNode) -> List[TreeNode]:
        count = collections.Counter()
        res = []
        def helper(root):
            if not root:
                return "#"
            serial = "{},{},{}".format(root.val, helper(root.left), helper(root.right))
            print(serial)
            count[serial] += 1
            if count[serial] == 2:
                res.append(root)
            return serial
        helper(root)
        return res
    
    
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        if not root: return []
        count = collections.Counter()
        res = []
        def reconstruct(root):
            if not root:
                return "#"
            reconstruct(root.left)
            reconstruct(root.right)
            return root
        def dfs(root):
            if not root:
                return
            serial = "{},{},{}".format(root.val, dfs(root.left), dfs(root.right))
            count[serial] += 1
            if count[serial] == 2:
                res.append(root)
            return serial
        dfs(reconstruct(root))
        return res
            

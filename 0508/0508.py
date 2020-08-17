# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        preq = collections.defaultdict(int)
        
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur_sum = node.val + left + right
            preq[cur_sum] += 1
            return cur_sum
        
        dfs(root)
        return [i for i ,j in preq.items() if j == max(preq.values())]
        

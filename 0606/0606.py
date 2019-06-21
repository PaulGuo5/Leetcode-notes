# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str1(self, t: TreeNode) -> str:
        if not t:
            return ""
        res = ""
        def dfs(t):
            nonlocal res
            if not t:
                return
            if not t.left and t.right:
                res+="("+str(t.val)
                res += "()"
                dfs(t.left)
                dfs(t.right)
                res+=")"
            else:
                res+="("+str(t.val)
                dfs(t.left)
                dfs(t.right)
                res+=")"
            return res
        string = dfs(t)
        ans = ""
        for i in range(1, len(string)-1):
            ans += string[i]
        return ans
    
    
    def tree2str(self, t: TreeNode) -> str:  
        if not t:
            return ""
        elif not t.left and not t.right:
            return "{}".format(t.val)
        elif not t.left and t.right:
            return "{}()({})".format(t.val, self.tree2str(t.right))
        elif t.left and not t.right:
            return "{}({})".format(t.val, self.tree2str(t.left))
        else:
            return "{}({})({})".format(t.val, self.tree2str(t.left), self.tree2str(t.right))
        

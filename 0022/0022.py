class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(cur, n, l, r, res):
            if r == n:
                res.append(cur)
                return
            if l < n:
                dfs(cur+"(", n, l+1, r, res)
            if r < l:
                dfs(cur+")", n, l, r+1, res)
        res = []
        dfs("", n, 0, 0, res)
        return res

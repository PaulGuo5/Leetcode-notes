class Solution:
    def numberOfPatterns1(self, m: int, n: int) -> int:
        # dfs bottom-up
        cross = {(1,3):2, (3,1):2, (1,9):5, (9,1):5, (4,6):5, (6,4):5, (2,8):5, (8,2):5, (3,7):5, (7,3):5, (1,7):4, (7,1):4, (3,9):6, (9,3):6, (7,9):8, (9,7):8}
        
        def dfs(vis, cur, remain):
            if remain == 0:
                return 1
            if remain < 0:
                return 0
            vis.add(cur)
            res = 0
            for i in range(1, 10):
                if i not in vis and ((cur, i) not in cross or cross[(cur, i)] in vis):
                    res += dfs(vis, i, remain-1)
            vis.remove(cur)
            return res
        
        
        res = 0
        for remain in range(m-1, n):
            res += dfs(set(), 1, remain)*4
            res += dfs(set(), 2, remain)*4
            res += dfs(set(), 5, remain)

        return res
    
    
    def numberOfPatterns(self, m: int, n: int) -> int:
        # dfs top-down
        cross = {(1,3):2, (3,1):2, (1,9):5, (9,1):5, (4,6):5, (6,4):5, (2,8):5, (8,2):5, (3,7):5, (7,3):5, (1,7):4, (7,1):4, (3,9):6, (9,3):6, (7,9):8, (9,7):8}
        
        res = 0
        def dfs(vis, path):
            nonlocal res
            if m <= len(path) <= n:
                res += 1
            if len(path) > n:
                return
            cur = path[-1] if path else None
            for new in range(1, 10):
                if not cur or new not in vis:
                    if (cur, new) not in cross or cross[(cur, new)] in vis:
                        vis.add(new)
                        dfs(vis, path+[new])
                        vis.remove(new)
        
        dfs(set(), [])
        
        return res

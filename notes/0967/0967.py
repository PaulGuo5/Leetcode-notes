class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        res = set()
        
        def dfs(pos, path):
            if pos == N:
                if len(path) == 1 or (len(path) > 1 and path[0] != "0"):
                    res.add(int("".join(path)))
                return 
            if not path:
                for i in range(0, 10):
                    dfs(pos+1, [str(i)])
            else:
                tmp = int(path[-1])
                if tmp + K < 10:
                    dfs(pos+1, path+[str(tmp+K)])
                if tmp - K >= 0:
                    dfs(pos+1, path+[str(tmp-K)])
        
        dfs(0, [])
        return list(res)

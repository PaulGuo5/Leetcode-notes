class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(pos, path, cnt):
            if cnt == 0:
                res.append(path)
            for i in range(pos, n+1):
                dfs(i+1, path+[i], cnt-1)
        dfs(1, [], k)
        return res

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(pos, cur, path, cnt):
            if cnt == 0:
                if cur == n:
                    res.append(path)
                return
            for i in range(pos, 10):
                tmp = cur + i
                if tmp <= n:
                    dfs(i+1, tmp, path+[i], cnt-1)
        
        dfs(1, 0, [], k)
        return res

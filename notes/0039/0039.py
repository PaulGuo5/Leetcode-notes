class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(cand, pos, cur, res, path):
            if cur == target: 
                res.append(path)
                return
            for i in range(pos, len(cand)):
                if cand[i] + cur <= target:
                    dfs(cand, i, cur+cand[i], res, path + [cand[i]])
        
        res = []
        dfs(candidates, 0, 0, res, [])
        return res

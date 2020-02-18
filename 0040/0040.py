class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(cand, pos, cur, path, res):
            if cur == target:
                res.append(path)
                return 
            for i in range(pos, len(cand)):
                if i > pos and cand[i] == cand[i-1]: continue
                if cur+cand[i] <= target:
                    dfs(cand, i+1, cur+cand[i], path+[cand[i]], res)
        
        res = []
        candidates.sort()
        dfs(candidates, 0, 0, [], res)
        return res

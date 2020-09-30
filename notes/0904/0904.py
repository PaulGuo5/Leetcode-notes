class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        fst = 0
        res = 0
        dic = {}
        for lst in range(len(tree)):
            if tree[lst] in dic:
                dic[tree[lst]] += 1
            elif tree[lst] not in dic:
                dic[tree[lst]] = 1
                
            while len(dic) > 2:
                dic[tree[fst]] -= 1
                if dic[tree[fst]] == 0:
                    del dic[tree[fst]]                
                fst += 1
                
            res = max(res, lst - fst + 1)
        return res
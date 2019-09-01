class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        cnt = 0
        dic = {}
        for d in dominoes:
            encode = max(d) * 10 + min(d)
            if encode not in dic:
                dic[encode] = 1
            else:
                cnt += dic[encode]
                dic[encode] += 1
        return cnt

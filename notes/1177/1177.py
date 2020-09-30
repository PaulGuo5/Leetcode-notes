class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnt = [[0]*26]
        for i in range(len(s)):
            cnt.append(cnt[i][:])
            cnt[i+1][ord(s[i])-ord('a')] += 1
        # res = []
        # for lo, hi, k in queries:
        #     s = 0
        #     for i in range(26):
        #         s += (cnt[hi+1][i] - cnt[lo][i]) %2
        #     if s//2 <= k:
        #         res.append(True)
        #     else:
        #         res.append(False)
        # return res
        
        return [sum((cnt[hi+1][i] - cnt[lo][i]) %2 for i in range(26)) // 2 <= k for lo, hi, k in queries]

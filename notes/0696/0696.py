class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        same = []
        cnt = 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                same.append(cnt)
                cnt = 1
        same.append(cnt)
        for i in range(len(same)-1):
            res += min(same[i], same[i+1])
        return res

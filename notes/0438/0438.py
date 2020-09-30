class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return []
        c = collections.Counter(p)
        res = []
        for i in range(len(s)-len(p)+1):
            if i == 0:
                cc = collections.Counter(s[i:i+len(p)])
            else:
                cc[s[i-1]] -= 1
                if cc[s[i-1]] == 0:
                    del cc[s[i-1]]
                cc[s[i+len(p)-1]] += 1
            if cc == c:
                res.append(i)
        return res

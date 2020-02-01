class Solution:
    def findReplaceString1(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        i = 0
        while i < len(S):
            if i in set(indexes) and S[i: i+len(sources[indexes.index(i)])] == sources[indexes.index(i)]:
                res += targets[indexes.index(i)]
                i += len(sources[indexes.index(i)])
            else:
                res += S[i]
                i += 1
        return res
    
    
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            S = S[:i] + t + S[i+len(s):] if S[i:i+len(s)] == s else S
        return S

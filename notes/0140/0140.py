class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s or not wordDict: return []
        res = []
        words = set(wordDict)
        dp = [0]*(len(s)+1)
        dp[0] = 1
        parent = collections.defaultdict(list)
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = 1
                    parent[i].append(j)
        def dfs(i, path):
            if i == 0:
                res.append((s[:i]+" "+path).strip())
                return
            for j in parent[i]:
                dfs(j, s[j:i]+" "+path)
            return res
        return dfs(len(s), "")
        

class Solution:
    def longestStrChain1(self, words: List[str]) -> int:
        def dfs(w1, size):
            return max([dfs(w2, size + 1) for w2 in graph[w1]], default = size)
        graph = collections.defaultdict(list)
        for w in words:
            graph[len(w)].append(w)
        for w1 in words:
            for w2 in graph[len(w1) + 1]:
                for i in range(len(w2)):
                    if w2[:i] + w2[i + 1:] == w1:
                        graph[w1].append(w2)
        return max(dfs(w, 1) for w in words)
    
    
    def longestStrChain2(self, words: List[str]) -> int:
        def dfs(w, length):
            return max([dfs(w1, length+1) for w1 in graph[w]] or [length])
                
        graph = collections.defaultdict(list)
        for w in words:
            graph[len(w)].append(w)
        for w1 in words:
            for w2 in graph[len(w1)+1]:
                for i in range(len(w2)):
                    if w2[:i] + w2[i+1:] == w1:
                        graph[w1].append(w2)
        return max(dfs(w, 1) for w in words)
    
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}
        for w in sorted(words, key = len):
            dp[w] = max(dp.get(w[:i]+w[i+1:], 0)+1 for i in range(len(w)))
        return max(dp.values())
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        iset = set(words)
        res = []
        for word in words:
            n = len(word)
            if not n:
                continue
            dp = [0]*(n+1)
            dp[0] = 1
            iset.remove(word)
            for i in range(1, n+1):
                for j in range(i):
                    if dp[j] == 1 and word[j:i] in iset:
                        dp[i] = 1
                        break
            if dp[n] == 1:
                res.append(word)
            iset.add(word)
        return res

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        n = len(words)
        res = n
        p1 = p2 = -n
        for i in range(n):
            if words[i] == word1:
                p1 = i
                res = min(res, i - p2)
            elif words[i] == word2:
                p2 = i
                res = min(res, i - p1)
        return res

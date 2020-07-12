class Solution:
    def findLongestWord(self, S: str, D: List[str]) -> str:
        D.sort(key = lambda x: (-len(x), x))
        for word in D:
            i = 0
            for c in S:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""

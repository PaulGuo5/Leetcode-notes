class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key = lambda x: (-len(x), x))
        d = set(words)
        for word in words:
            if all(word[:i] in d for i in range(1, len(word))):
                return word
        return ""

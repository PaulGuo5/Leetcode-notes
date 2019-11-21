class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res = 0
        c = collections.defaultdict(list)
        for i, j in enumerate(keyboard):
            c[j] = i
        pre = keyboard[0]
        for w in word:
            res += abs(c[w] - c[pre])
            pre = w
        return res

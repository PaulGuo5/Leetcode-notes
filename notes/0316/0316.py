class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i
        res = []
        for i, ch in enumerate(s):
            if ch not in res:
                while res and ch < res[-1] and i < last_index[res[-1]]:
                    res.pop()
                res.append(ch)
        return "".join(res)

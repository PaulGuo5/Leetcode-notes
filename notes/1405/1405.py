class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        d = {"a":a, "b":b, "c":c}
        while d["a"] != 0 or d["b"] != 0 or d["c"] != 0:
            char = [i for i, j in sorted(d.items(), key=lambda x: x[1], reverse = True) if j > 0]
            if char and len(s) > 1 and char[0] == s[-1] and char[0] == s[-2]:
                char = char[1:]
            if not char: break
            s += char[0]
            d[char[0]] -= 1
        return s

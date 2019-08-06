class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if g[i] > s[j]:
                j += 1
            else:
                i += 1
                j += 1
        return i

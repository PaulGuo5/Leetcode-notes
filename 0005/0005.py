class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getLen(s, l, r):
            if r >= len(s) or s[l] != s[r]:
                return 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
        start, end = 0, 0
        for i in range(len(s)):
            if i + (end - start) // 2 > len(s):
                break
            l = max(getLen(s, i, i), getLen(s, i, i+1))
            if l > end - start:
                start = i - (l - 1) // 2
                end = start + l
        return s[start:end]

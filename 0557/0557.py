class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        for i in range(len(s)):
            s[i] = s[i][::-1]
        res = ""
        for char in s:
            res += char + " "
        if res[-1] and res[-1] == " ":
            res = res[:-1]
        return res        

class Solution:
    def toLowerCase1(self, str: str) -> str:
        return str.lower()
    
    def toLowerCase(self, str: str) -> str:
        res = ""
        for c in str:
            if ord(c) >= ord("A") and ord(c) <= ord("Z"):
                res += chr(ord("a") + ord(c) - ord("A"))
            else:
                res += c
        return res

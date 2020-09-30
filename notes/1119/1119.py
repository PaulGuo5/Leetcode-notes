class Solution:
    def removeVowels(self, S: str) -> str:
        c = set("aeiou")
        res = ""
        for i in S:
            if i not in c:
                res += i
        return res

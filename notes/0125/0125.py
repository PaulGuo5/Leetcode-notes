class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for char in s:
            if char >= "A" and char <= "Z":
                res.append(char.lower())
            elif char >= "a" and char <= "z": 
                res.append(char)
            elif char.isdigit():
                res.append(char)
        fst, lst = 0, len(res)-1
        while fst < lst:
            if res[fst] != res[lst]:
                return False
            fst += 1
            lst -= 1
        return True

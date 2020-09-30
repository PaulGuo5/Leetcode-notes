class Solution:
    def checkPalindrome(self, s):
        fst = 0
        lst = len(s) - 1
        count = 0
        while fst < lst:
            if s[fst] == s[lst]:
                fst += 1
                lst -= 1
            else:
                return False
        return True

    def validPalindrome(self, s: str) -> bool:
        fst = 0
        lst = len(s) - 1
        while fst < lst:
            if s[fst] == s[lst]:
                fst += 1
                lst -= 1
            else:
                if self.checkPalindrome(s[fst: lst]) or self.checkPalindrome(s[fst + 1: lst + 1]):
                    return True
                else:
                    return False
        return True
            

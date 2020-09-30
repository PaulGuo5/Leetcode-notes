class Solution:
    def detectCapitalUse1(self, word: str) -> bool:
        def isCaptical(c):
            return True if ord(c) >= ord("A") and ord(c) <= ord("Z") else False
        if not word:
            return True
        if isCaptical(word[0]):
            if len(word) > 2:
                tmp = isCaptical(word[1])
                for c in word[2:]:
                    if isCaptical(c) != tmp:
                        return False
        else:
            for c in word[1:]:
                if isCaptical(c):
                    return False
        return True
    
    def detectCapitalUse(self, word: str) -> bool:
        res = [c.isupper() for c in word]
        return all(res) or not any(res) or (res[0] and not any(res[1:]))

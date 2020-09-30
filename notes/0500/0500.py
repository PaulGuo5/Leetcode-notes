class Solution:
    def findWords1(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        res = []
        for word in words:
            if word:
                if word[0] in row1:
                    flag = "row1"
                elif word[0] in row2:
                    flag = "row2"
                elif word[0] in row3:
                    flag = "row3"
            for w in word:
                if (w in row1 and flag != "row1") or (w in row2 and flag != "row2" )or (w in row3 and flag != "row3"):
                    f = 0
                    break
                else:
                    f = 1
            if f == 1:
                res.append(word)
        return res
    
    def findWords2(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        res = []
        for word in words:
            if set(word) <= row1 or set(word) <= row2 or set(word) <= row3:
                res.append(word)
        return res
    
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiopQWERTYUIOP")
        row2 = set("asdfghjklASDFGHJKL")
        row3 = set("zxcvbnmZXCVBNM")
        return [word for word in words if set(word) <= row1 or 
                                          set(word) <= row2 or 
                                          set(word) <= row3]       

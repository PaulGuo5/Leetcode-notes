class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = set("aeiouAEIOU")
        splited = S.split()
        res = ""
        for i in range(len(splited)):
            if splited[i][0] not in vowel:
                res += (splited[i][1:] + splited[i][0] + "ma" + "a"*(i+1) + " ")
            else:
                res += (splited[i] + "ma" + "a"*(i+1) + " ")
        return res[:-1]

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = []
        for s in S:
            if s.isalpha():
                letters.append(s)
        letters = letters[::-1]
        res = ""
        p = 0
        for i in range(len(S)):
            if S[i].isalpha():
                res+=letters[p]
                p+=1
            else:
                res+=S[i]
        return res

class Solution:
    def licenseKeyFormatting2(self, S: str, K: int) -> str:
        S = S.split("-")
        tmp = ""
        for char in S:
            tmp += char
        tmp = tmp[::-1]
        res = ""
        i = 1
        for char in tmp:
            char = char.upper()
            if i % K == 0:
                res += str(char) + "-"
            else:
                res += str(char)
            i += 1
        res = res[::-1]
        if not res:
            return res
        if res[0] == "-":
            res = res[1:]
        return res
    
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = ""
        count = 1
        for i in range(len(S)-1, -1, -1):
            if S[i] == "-":
                continue
            else:
                res += S[i].upper()
                if count % K == 0 and i < len(S):
                    res += "-"
                count += 1
        res = res[::-1]
        if not res:
            return res
        if res[0] == "-":
            res = res[1:]
        return res

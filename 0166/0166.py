class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pos = True if numerator*denominator >= 0 else False
        numerator, denominator = abs(numerator), abs(denominator)
        d, r = divmod(numerator, denominator)
        dic = {}
        if r == 0: 
            return str(d) if pos else "-"+str(d)
        res = str(d)+"."
        while r:
            dic[r] = len(res)
            r *= 10
            d, r = divmod(r, denominator)
            res += str(d)
            if r in dic:
                break
        res = res[:dic[r]] + "(" + res[dic[r]:] + ")" if r != 0 else res
        return res if pos else "-"+res

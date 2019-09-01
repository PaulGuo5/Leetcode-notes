class Solution:
    def bitwiseComplement1(self, N: int) -> int:
        b = bin(N)
        print(b)
        res = ""
        for i in range(2, len(b)):
            res += str(1 - int(b[i]))
        return int(res, 2)
    
    
    def bitwiseComplement(self, N: int) -> int:
        if N == 0 or N == 1:
            return 0 if N == 1 else 1
        def toBin(N, res):
            while True:
                if N == 0: 
                    return res[::-1]
                N, r = divmod(N, 2)
                res += str(r)
        def toInt(n):
            i = 0
            res = 0
            n = n[::-1]
            for j in n:
                res += 2**i*int(j)
                i += 1
            return res
        b = toBin(N, "")
        b_ = ""
        for i in b:
            b_ += str(1-int(i))
        return toInt(b_)

from itertools import zip_longest
class Solution:
    def addBinary2(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        carry = 0
        res = ""
        len_a = len(a)
        len_b = len(b)
        max_l = max(len_a, len_b)
        for i in range(max_l):
            if i < len_b:
                sum_ = int(a[-(i+1)]) + int(b[-(i+1)])
                carry, tmp = divmod((sum_ + carry), 2)
                res = str(tmp) + res
            else:
                carry, tmp = divmod((int(a[-(i+1)]) + carry), 2)
                res = str(tmp) + res
        if carry == 1:
            res = "1" + res
        
        return res


    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ""
        for a, b in zip_longest(a[::-1], b[::-1], fillvalue = 0):
            carry, tmp = divmod((int(a) + int(b) + carry), 2)
            res = str(tmp) + res
        if carry == 1:
            res = str(carry) + res
        return res

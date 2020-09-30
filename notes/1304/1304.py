class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [0]
        if n == 1:
            return res
        if n % 2 != 0:
            k = (n - 1) // 2
            while len(res) <= n and k!=0:
                res.append(k)
                res.append(-k)
                k = k-1
        else:
            k = n // 2
            res.remove(0)
            while len(res) <= n and k!=0:
                res.append(k)
                res.append(-k)
                k = k-1
        return res

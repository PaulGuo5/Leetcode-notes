class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = list(str(n))
        i = j = len(n)-1
        while i-1 >= 0 and n[i-1] >= n[i]:
            i -= 1
        i -= 1
        if i == -1:
            return -1
        while n[j] <= n[i]:
            j -= 1
        n[i], n[j] = n[j], n[i]
        res = int("".join(n[:i+1]+n[i+1:][::-1]))
        return -1 if res >= 2**31 or res <= -2**32 else res

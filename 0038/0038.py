class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        for r in range(1, n):
            pre = res[0]
            count = 0
            tmp = ""
            for char in res:
                if char == pre:
                    count += 1
                else:
                    tmp = tmp + str(count) + pre
                    pre = char
                    count = 1
            tmp = tmp + str(count) + pre
            res = tmp
        return res

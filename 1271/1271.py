class Solution:
    def toHexspeak(self, num: str) -> str:
        num = int(num)
        res = ""
        vows = set("ABCDEFIO")
        while num > 0:
            tmp = str(num % 16)
            if tmp == "1":
                tmp = 'I'
            elif tmp == '0':
                tmp = 'O'
            elif tmp == '10':
                tmp = 'A'
            elif tmp == '11':
                tmp = 'B'
            elif tmp == '12':
                tmp = 'C'
            elif tmp == '13':
                tmp = 'D'
            elif tmp == '14':
                tmp = 'E'
            elif tmp == '15':
                tmp = 'F'
            res += tmp
            num = num // 16
        for i in res:
            if i not in vows:
                return 'ERROR'
        return res[::-1]
        
        

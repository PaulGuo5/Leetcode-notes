class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(n):
            if n == 0: return [""]
            if n == 1: return ["0", "1", "8"]
            pre = helper(n-2)
            new = []
            for i in pre:
                new.append("0"+i+"0")
                new.append("1"+i+"1")
                new.append("6"+i+"9")
                new.append("9"+i+"6")
                new.append("8"+i+"8")
            return new
        
        res = helper(n)
        if n in (0,1):
            return res
        return [i for i in res if i[0] != "0"]

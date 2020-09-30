class Solution:
    def findStrobogrammatic1(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]
        
        table = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}
        nums = ("0", "1", "8")
        res = []
        
        def dfs(pos, path):
            if pos == n:
                if len(path) == 1 or (len(path) > 1 and path[0] != "0"):
                    res.append("".join(path))
                return
            if not path:
                for i in ("1", "8", "6", "9"):
                    dfs(pos+1, [i])
            else:
                if pos < n//2:
                    for i in ("0", "1", "8", "6", "9"):
                        dfs(pos+1, path+[i])
                else:
                    tmp_pos = n-pos-1
                    if tmp_pos >= len(path):
                        for i in nums:
                            dfs(pos+1, path+[i])
                    else:
                        dfs(pos+1, path+[table[path[tmp_pos]]])
        
        dfs(0, [])
        return res
    
    def findStrobogrammatic(self, n: int) -> List[str]:
        def dfs(n):
            if n == 0:
                return [""]
            if n == 1:
                return ["0", "1", "8"]
            pre = dfs(n-2)
            new = []
            for num in pre:
                new.append("0"+num+"0")
                new.append("1"+num+"1")
                new.append("8"+num+"8")
                new.append("6"+num+"9")
                new.append("9"+num+"6")
            return new
        
        res = dfs(n)
        if n in (0, 1):
            return res
        return [num for num in res if num[0] != "0"]
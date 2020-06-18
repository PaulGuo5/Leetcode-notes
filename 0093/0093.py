class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(s, index, path, res):
            if index == 4:
                if not s:
                    res.append(path[:-1])
                return
            
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        dfs(s[i:], index+1, path+s[:i]+".", res)
                    elif i == 2 and s[0] != "0":
                        dfs(s[i:], index+1, path+s[:i]+".", res)
                    elif i == 3 and s[0] != "0" and 0 <= int(s[:i]) <= 255:
                        dfs(s[i:], index+1, path+s[:i]+".", res)
        
        res = []
        dfs(s, 0, "", res)
        return res

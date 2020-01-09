class Solution:
    def confusingNumberII1(self, N: int) -> int:
        rotated = {0:0,1:1,6:9,8:8,9:6}
        self.res = 0
        def dfs(num, rotation, digit):
            if num != rotation:
                self.res += 1
            for i in rotated:
                if i == 0 and num == 0:
                    continue
                if num*10+i <= N:
                    dfs(num*10+i, rotated[i]*digit+rotation, digit*10)
            return self.res
        return dfs(0, 0, 1)
    
    
    def confusingNumberII(self, N: int) -> int:
        rotated = {0:0,1:1,6:9,8:8,9:6}
        self.res = 0
        def dfs(num, rotation, digit):
            if num != rotation:
                self.res += 1
            for i in rotated:
                if num*10+i <= N:
                    dfs(num*10+i, rotated[i]*digit+rotation, digit*10)
            
        dfs(1, 1, 10)
        dfs(6, 9, 10)
        dfs(8, 8, 10)
        dfs(9, 6, 10)
        
        return self.res
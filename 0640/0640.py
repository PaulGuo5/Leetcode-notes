class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")[0], equation.split("=")[1]
        def helper(s):
            flag = 1 #1 means +; -1 means -
            num_x = 0
            num_n = 0
            cur_num = ""
            for c in s:
                if c == "x":
                    if not cur_num: 
                        num_x += flag*1
                    else:
                        num_x += flag*(int(cur_num))
                    cur_num = ""
                elif c == "+":
                    if cur_num: 
                        num_n += flag*(int(cur_num))
                        cur_num = ""
                    flag = 1
                elif c == "-":
                    if cur_num: 
                        num_n += flag*(int(cur_num))
                        cur_num = ""
                    flag = -1
                else:
                    cur_num += str(c)
            if s[-1].isdigit():
                num_n += flag*(int(cur_num))
            return num_x, num_n
        
        x1, n1 = helper(left)
        x2, n2 = helper(right)
        r_x, r_n = x1 - x2, n2 - n1
        if r_x == 0 and r_n == 0: return "Infinite solutions"
        if r_x == 0: return "No solution"
        return "x="+ str(r_n//r_x)

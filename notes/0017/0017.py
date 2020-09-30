class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        def dfs(l, string, res):
            if l == len(digits):
                res.append(string)
                return
            for i in table[digits[l]]:
                dfs(l+1, string + i, res)
        table = {
            "2":["a", "b", "c"], 
            "3":["d", "e", "f"], 
            "4":["g", "h", "i"], 
            "5":["j", "k", "l"], 
            "6":["m" ,"n", "o"], 
            "7":["p", "q", "r", "s"], 
            "8":["t", "u", "v"], 
            "9":["w", "x", "y", "z"]
        }
        res = []
        dfs(0, '', res)
        return res

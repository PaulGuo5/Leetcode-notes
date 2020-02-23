class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows >= len(s) or numRows <= 1: return s
        line, step = 0, -1
        res = [""]*numRows
        for c in s:
            res[line] += c
            if line%(numRows-1) == 0:
                step = -step
            line += step
        return "".join(res)

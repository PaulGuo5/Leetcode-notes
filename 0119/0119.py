class Solution:
    def getRow1(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        rows = [[] for _ in range(rowIndex+1)]
        rows[0].append([1])
        rows[1] += [1,1]
        for i in range(2, rowIndex+1):
            len_ = i+1
            rows[i].append(1)
            for j in range(1, len_-1):
                rows[i] += [rows[i-1][j-1]+rows[i-1][j]]
            rows[i].append(1)
        return rows[-1]
    
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

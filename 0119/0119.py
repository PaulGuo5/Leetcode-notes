class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowNum = rowIndex + 1
        if rowNum == 0:
            return []
        if rowNum ==1:
            return [1]
        res=[[1]]
        for i in range(1, rowNum):
            row = []
            row.append(1)
            if i > 1: 
                for j in range(1, i):
                    row.append(lastRow[j-1] + lastRow[j])
            row.append(1)
            lastRow = row
        
        return row
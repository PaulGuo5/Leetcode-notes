class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if not coordinates: return False
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        if x2 == x1:
            pre = float('inf')
        else: pre = (y1-y2) / (x1-x2)
        for n1, n2 in zip(coordinates, coordinates[1:]):
            x1, y1 = n1
            x2, y2 = n2
            if x2 == x1:
                tmp = float('inf')
            else:
                tmp = (y1-y2) / (x1-x2)
            if tmp != pre:
                return False
            pre = tmp
        return True

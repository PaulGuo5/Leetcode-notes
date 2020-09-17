class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        di = (-1, 0)
        pos = (0, 0) 
        for i in instructions:
            if i == "G":
                pos = pos[0]+di[0], pos[1]+di[1]
            elif i == "L":
                di = -di[1], di[0]
            else:
                di = di[1], -di[0]
        
        return pos == (0, 0) or di != (-1, 0)

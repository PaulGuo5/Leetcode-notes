class Solution:
    def judgeCircle(self, moves: str) -> bool:
        dic_horizon = {"R":1, "L":-1}
        dic_vertical = {"U": 1, "D":-1}
        sum_horizon = 0
        sum_vertical = 0
        for m in moves:
            if m in dic_horizon:
                sum_horizon += dic_horizon[m]
            if m in dic_vertical:
                sum_vertical += dic_vertical[m]
        return True if sum_horizon == 0 and sum_vertical == 0 else False

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        j = 0
        for i in range(len(houses)):
                while j < len(heaters) - 1 and abs(heaters[j]-houses[i]) >= abs(heaters[j+1]-houses[i]):
                    j += 1
                res = max(abs(heaters[j]-houses[i]), res)
        return res

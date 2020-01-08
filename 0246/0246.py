class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated = {"1":"1", "6":"9", "8":"8", "9":"6","0":"0"}
        new = ""
        for i in num:
            if i not in rotated:
                return False
            new += rotated[i]
        return new[::-1] == num

from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        split_1 = version1.split(".")
        split_2 = version2.split(".")
        for split_1, split_2 in zip_longest(split_1, split_2, fillvalue = "0"):
            if int(split_1) > int(split_2):
                return 1
            elif int(split_1) < int(split_2):
                return -1
            elif int(split_1) == int(split_2):
                continue 
        return 0

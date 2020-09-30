class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_m = {}
        for c in list(magazine):
            if c not in dict_m:
                dict_m[c] = 1
            else:
                dict_m[c] += 1
        for c in list(ransomNote):
            if c not in dict_m.keys() or dict_m[c] < 1:
                return False
            else:
                dict_m[c] -= 1
        return True

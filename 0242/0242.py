class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1, dict_2 = {}, {}
        for c in s:
            if c not in dict_1:
                dict_1[c] = 1
            else:
                dict_1[c] += 1
        for c in t:
            if c not in dict_2:
                dict_2[c] = 1
            else:
                dict_2[c] += 1
        if dict_1 == dict_2:
            return True
        return False

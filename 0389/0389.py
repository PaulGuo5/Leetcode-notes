class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict, t_dict = {}, {}
        for c in list(s):
            if c not in s_dict:
                s_dict[c] = 1
            else:
                s_dict[c] += 1
        for c in list(t):
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1
        for i, j in t_dict.items():
            if i not in s_dict.keys() or (i in s_dict.keys() and s_dict[i] != t_dict[i]):
                return i

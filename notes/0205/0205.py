class Solution:
    def isIsomorphic2(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        i = 1
        res_s = ""
        for char in s:
            if char not in dict_s:
                dict_s[char] = i
                res_s += "i"
                i += 1
            else:
                res_s += str(dict_s[char])
        i = 1
        res_t = ""
        for char in t:
            if char not in dict_t:
                dict_t[char] = i
                res_t += "i"
                i += 1
            else:
                res_t += str(dict_t[char])
        if res_t == res_s:
            return True
        return False
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        value_set = set()
        for char_s, char_t in zip(s,t):
            if char_s in char_map and char_map[char_s] != char_t:
                return False
            elif char_s not in char_map and char_t in value_set:
                return False
            elif char_s not in char_map:
                char_map[char_s] = char_t
                value_set.add(char_t)
        return True
                

from collections import defaultdict
class Solution:
    def groupAnagrams1(self, strs):
        str_map = {}
        for string in strs:
            tmp = "".join(sorted(string))
            if tmp not in str_map:
                str_map[tmp] = [string]
            else:
                str_map[tmp].append(string)
        return list(str_map.values())
    
    def groupAnagrams(self, strs):
        str_map = defaultdict(list)
        for string in strs:
            str_map["".join(sorted(string))].append(string)
        return list(str_map.values())

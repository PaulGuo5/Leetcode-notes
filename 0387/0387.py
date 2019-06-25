from collections import Counter
class Solution:
    def firstUniqChar1(self, s: str) -> int:
        count_dict = {}
        res = -1
        for char in s:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for key in count_dict:
            if count_dict[key] == 1:
                res = key
                for index in range(len(s)):
                    if s[index] == res:
                        return index
        return res
    
    def firstUniqChar2(self, s: str) -> int:
        count_dict = {}
        for char in s:
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
        for index, char in enumerate(s):
            if count_dict[char] == 1:
                return index
        return -1
    
    def firstUniqChar(self, s: str) -> int:
        count_s = Counter(s)
        for index, char in enumerate(s):
            if count_s[char] == 1:
                return index
        return -1

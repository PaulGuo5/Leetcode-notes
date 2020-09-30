class Solution:
    def wordPattern1(self, pattern: str, str: str) -> bool:
        dict_ = {}
        str = str.split(" ")
        if len(pattern) != len(str):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict_:
                if str[i] in dict_.values():
                    return False
                dict_[pattern[i]] = str[i]
            else:
                if dict_[pattern[i]] != str[i]:
                    return False
        return True

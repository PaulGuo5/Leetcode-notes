class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, start, dic = 0, 0, {}
        for i, char in enumerate(s):
            if char in dic:
                res = max(res, i - start)
                start = max(start, dic[char] + 1)
            dic[char] = i
        return max(res, len(s) - start)

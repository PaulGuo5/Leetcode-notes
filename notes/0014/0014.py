class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for index, letters in enumerate(zip(*strs)):
            if len(set(letters)) == 1:
                res += letters[0]
            else:
                break
        return res

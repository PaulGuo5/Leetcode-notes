class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        fst, lst = 0, len(s)-1
        while fst < lst:
            s[fst], s[lst] = s[lst], s[fst]
            fst += 1
            lst -= 1

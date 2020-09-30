class Solution:
    def hIndex(self, citations: List[int]) -> int:
        l, r = 0, len(citations)-1
        while l <= r:
            m = (l+r) // 2
            if len(citations)-m == citations[m]:
                return len(citations)-m
            if len(citations)-m > citations[m]:
                l = m + 1
            else:
                r = m - 1
        return len(citations)-l

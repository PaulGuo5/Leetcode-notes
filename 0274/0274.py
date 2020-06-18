class Solution:
    def hIndex(self, citations: List[int]) -> int:
        for i, c in enumerate(sorted(citations)):
            if len(citations) - i <= c:
                return len(citations) - i
        return 0

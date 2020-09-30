class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        sum_ = 0
        line = 1
        for s in S:
            pos = ord(s) - ord("a")
            if (sum_ + widths[pos]) > 100:
                line += 1
                sum_ = widths[pos]
            else:
                sum_ += widths[pos]
        return [line, sum_]

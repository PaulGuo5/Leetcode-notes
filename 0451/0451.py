class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join([i*j for i, j in sorted(collections.Counter(s).items(), key=lambda x: x[1], reverse=True)])

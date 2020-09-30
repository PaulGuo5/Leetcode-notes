class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i for i, j in sorted(collections.Counter(sorted(words)).items(), key=lambda x:x[1], reverse=True)[:k]]

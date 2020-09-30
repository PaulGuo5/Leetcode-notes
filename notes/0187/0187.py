class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        table = collections.defaultdict(int)
        for i in range(len(s)-9):
            table[s[i:i+10]] += 1
        return [i for i, j in table.items() if j > 1]

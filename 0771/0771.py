class Solution:
    def numJewelsInStones2(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            for j in J:
                if s == j:
                    count += 1
        return count
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for s in S:
            if s in set(J):
                count += 1
        return count

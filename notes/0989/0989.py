class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        return [ i for i in str(int("".join(map(str,A))) + K)]

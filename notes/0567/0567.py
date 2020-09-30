class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = collections.Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            if collections.Counter(s2[i:len(s1)+i]) == cnt:
                return True
        return False

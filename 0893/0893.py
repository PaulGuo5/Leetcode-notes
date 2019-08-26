class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        r = set()
        for i in A:
            odd = "".join(sorted(i[::2]))
            even = "".join(sorted(i[1::2]))
            r.add(odd+even)
        return len(r)

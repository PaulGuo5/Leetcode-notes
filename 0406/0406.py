class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_sorted = sorted(people, key=lambda x: (-x[0], x[1]))
        res = []
        for p, idx in people_sorted:
            res.insert(idx, (p, idx))
        return res

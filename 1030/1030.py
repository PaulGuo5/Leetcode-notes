class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        distances = []
        for r in range(R):
            for c in range(C):
                distances.append((abs(r0 - r) + abs(c0 - c), r, c))
        distances.sort(key = lambda x:x[0])
        return [(dist[1], dist[2]) for dist in distances]

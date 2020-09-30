class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        a, b = min(start, destination), max(start, destination)
        return min(sum(distance[a:b]), sum(distance[:a]) + sum(distance[b:]))

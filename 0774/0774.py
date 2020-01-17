class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        left, right = 0, stations[-1] - stations[0]
        while left + 1e-6 <= right:
            mid = (left+right) / 2
            count = 0
            for s1, s2 in zip(stations, stations[1:]):
                count += math.floor((s2-s1)//mid)
            if count > K:
                left = mid
            else:
                right = mid
        return left

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, total, sum_ = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i]-cost[i]
            sum_ += gas[i]-cost[i]
            if sum_ < 0:
                start = i + 1
                sum_ = 0
        return start if total >= 0 else -1

class Solution:
    def reachNumber1(self, target: int) -> int:
        target = abs(target)
        if not target:
            return 0
        total = 0
        step = 1
        while True:
            total += step
            if (total - target) % 2 == 0 and total >= target:
                return step
            step += 1
        return -1
    
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        if not target:
            return 0
        total = 0
        step = 1
        while True:
            total += step
            if total % 2 == target % 2 and total >= target:
                return step
            step += 1
        return -1

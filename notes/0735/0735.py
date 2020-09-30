class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            if not res:
                res.append(a)
            else:
                if res[-1] < 0 or a > 0:
                    res.append(a)
                else:
                    while res and res[-1] > 0:
                        if a + res[-1] == 0:
                            res.pop()
                            break
                        elif a + res[-1] < 0:
                            res.pop()
                            if not res or res[-1] < 0:
                                res.append(a)
                                break
                        else:
                            break
        return res

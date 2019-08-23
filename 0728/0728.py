class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def helper(n, map_):
            for i in map_:
                if n % int(i) != 0:
                    return False
            return True
        res = []
        for n in range(left, right+1):
            if "0" in str(n):
                continue
            map_ = set()
            for i in str(n):
                map_.add(i)
            if helper(n, map_):
                res.append(n)
        return res

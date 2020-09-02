class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if t == 0 else n//t
            for m in (dic.get(key), dic.get(key-1), dic.get(key+1)):
                if m is not None and abs(n - m) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = n
        return False

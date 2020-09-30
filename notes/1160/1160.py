class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        map_ = collections.Counter(chars)
        for w in words:
            map_w = collections.Counter(w)
            flag = 1
            for i, j in map_w.items():
                if i not in map_ or (i in map_ and j > map_[i]):
                    flag = 0
            if flag:
                res += len(w)
        return res

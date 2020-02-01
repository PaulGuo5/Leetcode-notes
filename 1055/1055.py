class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        set_source = set(source)
        for i in list(set(target)):
            if i not in set_source:
                return -1
        
        idx_s, idx_t = 0, 0
        while idx_t < len(target):
            if target[idx_t] == source[idx_s%len(source)]:
                idx_t += 1
            idx_s += 1
        return idx_s//len(source)+1 if idx_s%len(source) else idx_s//len(source)

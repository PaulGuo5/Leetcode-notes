class Solution:
    def minWindow1(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        table = collections.Counter(t)
        slow = 0
        matchCount = 0
        min_len = float("inf")
        start = 0
        for fast in range(len(s)):
            table[s[fast]] -= 1
            if table[s[fast]] >= 0:
                matchCount += 1
            while matchCount == len(t):
                if min_len > fast - slow + 1:
                    min_len = fast - slow + 1
                    start = slow
                table[s[slow]] += 1
                if table[s[slow]] > 0:
                    matchCount -= 1
                slow += 1
        return "" if min_len == float("inf") else s[start:start+min_len]
    
    
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        table = collections.Counter(t)
        slow = 0
        res = ""
        min_len = float("inf")
        match_cnt = 0
        for fast in range(len(s)):
            if s[fast] not in table:
                continue
            table[s[fast]] -= 1
            if table[s[fast]] >= 0:
                match_cnt += 1
            while match_cnt == len(t):
                if fast - slow + 1 < min_len:
                    min_len = fast - slow + 1
                    res = s[slow: fast+1]
                if s[slow] not in table:
                    slow += 1
                    continue
                table[s[slow]] += 1
                if table[s[slow]] >= 1:
                    match_cnt -= 1
                slow += 1
        print(table)
        return res

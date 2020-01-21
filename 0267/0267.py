class Solution:
    def generatePalindromes1(self, s: str) -> List[str]:
        l = [x for x in s]
        res = []
        used = set()
        def backtrack(first):
            if first == len(l):
                tmp = "".join(l[:])
                if tmp not in used and tmp[::-1] == tmp[:]:
                    res.append(tmp)
                    used.add(tmp)
            for i in range(first, len(l)):
                l[i], l[first] = l[first], l[i]
                backtrack(first+1)
                l[i], l[first] = l[first], l[i]
        backtrack(0)
        return list(res)
    
    def generatePalindromes(self, s: str) -> List[str]:
        res, path = [], []
        if not s: return []
        c = collections.Counter(s)
        odds = [i for i in c if c[i] %2 == 1]
        if len(odds) > 1: return []
        if odds: c[odds[0]] -= 1
        def helper(l):
            if l == 0: res.append(''.join(path+odds+path[::-1]))
            for letter in c:
                if c[letter] <= 0: continue
                c[letter] -= 2
                path.append(letter)
                helper(l-2)
                c[letter] += 2
                path.pop()
        helper(len(s)-1 if odds else len(s))
        return res

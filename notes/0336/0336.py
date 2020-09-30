class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            # return word[::-1] == word
            len_ = len(word)
            for x in range(len_//2):
                if word[x] != word[len_-x-1]:
                    return False
            return True
            
        res = set()
        table = collections.defaultdict(list)
        for i, w in enumerate(words):
            table[w] = i
            
        for i, w in enumerate(words):
            if isPalindrome(w) and "" in table and i != table[""]:
                res.add((i, table[""]))
                res.add((table[""], i))
                
            if w[::-1] in table and table[w[::-1]] != i:
                res.add((i, table[w[::-1]]))
                res.add((table[w[::-1]], i))

            
            for x in range(1, len(w)):
                left, right = w[:x], w[x:]
                rleft, rright = left[::-1], right[::-1]
                if isPalindrome(left) and rright in table:
                    res.add((table[rright], i))
                if isPalindrome(right) and rleft in table:
                    res.add((i, table[rleft]))
        return res

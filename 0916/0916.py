class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dic = collections.defaultdict(int)
        res = []
        for word in B:
            for letter in word:
                if letter not in dic:
                    dic[letter] = 1
                else:
                    dic[letter] = max(dic[letter], word.count(letter))
        
        for word in A:
            check = 0
            for letter in dic:
                if word.count(letter) >= dic[letter]:
                    check +=1
            if check == len(dic):
                res.append(word)

        return res

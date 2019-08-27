class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {j:i for i,j in enumerate(order)}
        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for i, j in zip(a, b):
                if dic[i] > dic[j]:
                    return False
                if dic[i] < dic[j]:
                    break
        return True

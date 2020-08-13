class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.chars = characters
        self.l = combinationLength
        self.coms = self.createComb(self.chars, self.l)
    
    def createComb(self, chars, l):
        if not chars or not l:
            return None
        res = []
        def dfs(pos, path, k):
            if k == l:
                res.append("".join(path))
                return
            for i in range(pos, len(chars)):
                dfs(i+1, path+[chars[i]], k+1)
        dfs(0, [], 0)
        return res
    
    def next(self) -> str:
        if self.coms:
            return self.coms.pop(0)

    def hasNext(self) -> bool:
        if self.coms:
            return True
        return False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

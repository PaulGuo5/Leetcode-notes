class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node['#'] = word
    def search(self, word, cur = None):
        if not cur: cur = self.root
        for w in word:
            if w not in cur:
                return []
            cur = cur[w]
        ret = []
        for w in cur:
            if w == "#":
                ret.append(cur[w])
            else:
                ret += self.search('', cur[w])
        return ret
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.dict = {}
        for i, s in enumerate(sentences):
            self.dict[s] = times[i]
        self.trie = Trie()
        for s in sentences:
            self.trie.insert(s)
        self.keyword = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.dict[self.keyword] = self.dict.get(self.keyword, 0) + 1
            self.trie.insert(self.keyword)
            self.keyword = ""
            return []
        self.keyword += c
        res = self.trie.search(self.keyword)
        res.sort(key = lambda x: (-self.dict[x], x))
        return res[:3]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)

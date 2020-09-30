class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.weight = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, i):
        node = self.root
        node.weight.append(i)
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.weight.append(i)
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.weight
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.pre = Trie()
        self.suf = Trie()
        
        for i, w in enumerate(list(words)):
            self.pre.insert(w, i)
            self.suf.insert(w[::-1], i)

    def f(self, prefix: str, suffix: str) -> int:
        p = self.pre.search(prefix)
        s = self.suf.search(suffix[::-1])
        i, j = len(p)-1, len(s)-1
        while i >= 0 and j >= 0:
            if p[i] == s[j]: return p[i]
            elif p[i] < s[j]: j -= 1
            else:  i -= 1
        return -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

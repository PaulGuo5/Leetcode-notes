class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.words = []
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.words.append(word)
            node.words.sort()
            while len(node.words) > 3:
                node.words.pop()
    
    def search(self, word):
        res = []
        node = self.root
        for c in word:
            if c not in node.children:
                break
            node = node.children[c]
            res.append(node.words[:])
        l_remain = len(word) - len(res)
        for _ in range(l_remain):
            res.append([])
        return res
            
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for prod in products:
            trie.insert(prod)
        return trie.search(searchWord)        

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.words = set()
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
            node.words.add(word)
    def searchWords(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return []
            node = node.children[c]
        return node.words
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie = Trie()
        res = []
        for word in words:
            trie.insert(word)
        
        def dfs(i, cur):
            if i == len(words[0]):
                res.append(cur)
                return
            tmp = "".join([row[i] for row in cur])
            if tmp:
                for word in trie.searchWords(tmp):
                    dfs(i+1, cur+[word])
        
        for word in words:
            dfs(1, [word])
        return res
    
    def wordSquares1(self, words: List[str]) -> List[List[str]]:
        pref, res = collections.defaultdict(set), []
        for word in words:
            for i in range(len(word)):
                pref[word[:i+1]].add(word)
        
        def dfs(i, cur):
            if i == len(words[0]):
                res.append(cur)
                return
            for word in pref["".join([row[i] for row in cur])]:
                dfs(i+1, cur+[word])
        
        for word in words:
            dfs(1, [word])
        return res

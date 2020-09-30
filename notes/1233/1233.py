class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isWord = True
    def find(self):
        res = []
        def dfs(node, path):
            if node.isWord:
                res.append("/"+"/".join(path))
                return
            for c in node.children:
                dfs(node.children[c], path+[c])
        dfs(self.root, [])
        return res
    
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        for f in folder:
            trie.insert(f.split("/")[1:])
        return trie.find()
        

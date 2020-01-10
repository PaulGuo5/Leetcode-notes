class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, "", i, j, res)
        return res
    def dfs(self, board, node, path, i, j, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        cur = board[i][j]
        node = node.children.get(cur)
        if not node:
            return
        board[i][j] = '#'
        self.dfs(board, node, path+cur, i+1, j, res)
        self.dfs(board, node, path+cur, i-1, j, res)
        self.dfs(board, node, path+cur, i, j+1, res)
        self.dfs(board, node, path+cur, i, j-1, res)
        board[i][j] = cur

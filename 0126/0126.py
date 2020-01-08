class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList: return []
        queue = collections.deque([(beginWord, 1)])
        graph = collections.defaultdict(set)
        visited = set([beginWord])
        distance = {}
        while queue:
            word, dist = queue.popleft()
            distance[word] = dist
            for i in range(len(word)):
                for j in 'abcdefghijklmnopqrstuvwxyz':
                    if j != word[i]:
                        new = word[:i] + j + word[i+1:]
                        if new in wordList:
                            graph[new].add(word)
                            graph[word].add(new)
                            if new not in visited:
                                queue.append((new, dist+1))
                                visited.add(new)
        tmp, res = [], []
        def dfs(word):
            tmp.append(word)
            if word == endWord:
                res.append(list(tmp))
                tmp.pop()
                return
            if word in graph:
                for v in graph[word]:
                    if distance[v] == distance[word]+1:
                        dfs(v)
            tmp.pop()
        
        dfs(beginWord)
        return res
        

class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        len_w1, len_w2 = len(words1), len(words2)
        if len_w1 != len_w2: return False
        graph = collections.defaultdict(set)
        for p in pairs:
            graph[p[0]].add(p[1])
            graph[p[1]].add(p[0])
        for i in range(len_w1):
            if words1[i] != words2[i] and not self.dfs(words1[i], words2[i], graph, visited = set()):
                return False
        return True
    
    def dfs(self, word, target, graph, visited):
        if word == target: return True
        visited.add(word)
        for nei in graph[word]:
            if nei not in visited:
                if self.dfs(nei, target, graph, visited):
                    return True
        return False

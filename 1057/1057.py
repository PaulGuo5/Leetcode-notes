class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        dis = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                d = abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
                dis.append((d, i, j))
        dis.sort()
        
        visited = set()
        res = [-1]*len(workers)
        for d, w, b in dis:
            if res[w] == -1 and b not in visited:
                res[w] = b
                visited.add(b)
        return res

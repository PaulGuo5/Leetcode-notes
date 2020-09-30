class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0]*N
        graph = [[] for i in range(N)]
        for path in paths:
            graph[path[0]-1].append(path[1]-1)
            graph[path[1]-1].append(path[0]-1)
        for i in range(N):
            n_colors = []
            for n in graph[i]:
                n_colors.append(res[n])
            for flower in [1, 2, 3, 4]:
                if flower in n_colors:
                    continue
                res[i] = flower
                break
        return res
                

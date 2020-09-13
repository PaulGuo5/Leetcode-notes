class Solution:
    def floodFill1(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # bfs
        if not image:
            return image
        m, n = len(image), len(image[0])
        
        start_color = image[sr][sc]
        q = collections.deque([(sr, sc)])
        vis = set()
        while q:
            i, j = q.popleft()
            image[i][j] = newColor
            for ii, jj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i+ii, j+jj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis and image[ni][nj] == start_color:
                    vis.add((ni, nj))
                    q.append((ni, nj))
        return image
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # dfs
        if not image:
            return image
        m, n = len(image), len(image[0])
        vis = set()
        start_color = image[sr][sc]
        vis.add((sr, sc))
        
        def dfs(i, j):
            image[i][j] = newColor
            for ii, jj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                ni, nj = i+ii, j+jj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in vis and image[ni][nj] == start_color:
                    vis.add((ni, nj))
                    dfs(ni, nj)
        
        dfs(sr, sc)
        return image

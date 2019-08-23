class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def dfs(image, sr, sc, newColor, color):
            directions = [(0,-1), (1,0), (0,1), (-1,0)]
            image[sr][sc] = newColor
            for d in directions:
                r = sr + d[0]
                c = sc + d[1]
                if 0 <= r < len(image) and 0 <= c < len(image[0]) and color == image[r][c]:
                    dfs(image, r, c, newColor, color)
        color = image[sr][sc]
        if newColor == color:
            return image
        dfs(image, sr, sc, newColor, color)
        return image

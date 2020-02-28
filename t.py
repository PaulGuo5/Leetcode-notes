# m = int(input())
# n = int(input())
# grid = [[0]*n for _ in range(m)]
# for i in range(m):
# 	for j in range(n):
# 		grid[i][j] = int(input())


def bfs(grid, visited, s, e):
	res = 0
	dirs = {(1,0),(-1,0),(0,1),(0,-1)}
	m, n = len(grid), len(grid[0])
	q = [(s,e)]
	visited.add((s,e))
	dist = 0
	while q:
		sz = len(q)
		for i in range(sz):
			cur = q[0]
			q.pop(0)
			found = False
			for d in dirs:
				x = d[0] + cur[0]
				y = d[1] + cur[1]
				if x < 0 or y < 0 or x >= m or y >= n or (x,y) in visited or grid[x][y] == "#": continue
				if grid[x][y] == "$":
					found = True
					res += dist + 1
					res += bfs(grid, visited, x, y)
			if not found:
				for d in dirs:
					x = d[0] + cur[0]
					y = d[1] + cur[1]
					if x < 0 or y < 0 or x >= m or y >= n or (x,y) in visited or grid[x][y] == "#": continue
					res += dist+1
					q.append((x,y))
					visited.add((x,y))
		dist += 1

	return res



grid = [["$","$"],["#","."]]

res = 0
visited = set()
print(bfs(grid, visited, 0, 0))
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def move(x, y, m, direction, ob):
            for i in range(m):
                if direction == 0:
                    y += 1
                    if (x,y) in ob:
                        y -= 1
                        return x,y
                if direction == 1:
                    x += 1
                    if (x,y) in ob:
                        x -= 1
                        return x,y
                if direction == 2:
                    y -= 1
                    if (x,y) in ob:
                        y += 1
                        return x,y
                if direction == 3:
                    x -= 1
                    if (x,y) in ob:
                        x += 1
                        return x,y
            return x,y
        
        
        x, y = 0, 0
        direction = 0
        max_d = 0
        obstacles = set(map(tuple, obstacles))
        for c in commands:
            if c == -1:
                direction = (direction + 1) % 4
            if c == -2:
                direction = (direction -1) % 4
            else: 
                x, y = move(x, y, c, direction, obstacles)
                max_d = max(max_d, x**2 + y**2)
        return max_d
                    

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.width = width
        self.height = height
        self.food = food
        self.body = collections.deque([(0,0)])
        self.food_ind = 0

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        i, j = self.body[-1]
        if direction == "U": i -= 1
        elif direction == "D": i += 1
        elif direction == "L": j -= 1
        elif direction == "R": j += 1
        if i >= self.height or i < 0 or j >= self.width or j < 0 or ((i,j) in set(self.body) and (i,j) != self.body[0]): return -1
        self.body.append((i, j))
        if self.food_ind < len(self.food):
            x, y = self.food[self.food_ind]
            if i == x and j == y:
                self.food_ind += 1
                return self.food_ind
        tmp = self.body.popleft()
        return self.food_ind 


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

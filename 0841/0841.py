class Solution:
    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        self.visited = set()
        def dfs(i):
            if i in self.visited: return 
            self.visited.add(i)
            for i in rooms[i]:
                dfs(i)
        dfs(0)
        return len(self.visited) == len(rooms)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = set()
        q = collections.deque([0])
        while q:
            i = q.popleft()
            self.visited.add(i)
            for j in rooms[i]:
                if j not in self.visited:
                    q.append(j)
                    
        return len(self.visited) == len(rooms)

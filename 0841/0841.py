class Solution:
    def canVisitAllRooms1(self, rooms: List[List[int]]) -> bool:
        # dfs
        if not rooms:
            return True
        
        vis = set()
        
        def dfs(i):
            nonlocal vis
            vis.add(i)
            for key in rooms[i]:
                if key not in vis:
                    dfs(key)
        
        dfs(0)
        return len(vis) == len(rooms)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # bfs
        if not rooms:
            return True
        
        q = collections.deque([0])
        vis = set()
        while q:
            room = q.popleft()
            vis.add(room)
            for j in rooms[room]:
                if j not in vis:
                    q.append(j)
        return len(vis) == len(rooms)

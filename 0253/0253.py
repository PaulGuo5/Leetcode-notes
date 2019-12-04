class Solution:
    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        used_rooms = 0
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        end_pointer = 0
        start_pointer = 0

        while start_pointer < L:
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                used_rooms -= 1
                end_pointer += 1
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms
    
    
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0
        intervals.sort()
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if i[0] >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)

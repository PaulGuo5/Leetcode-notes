class Solution:
    def networkDelayTime1(self, times: List[List[int]], N: int, K: int) -> int:
        t = [0] + [float('inf')]*N
        graph = collections.defaultdict(list)
        q = collections.deque([(0, K)])
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = q.popleft()
            if time < t[node]:
                t[node] = time
                for n, w in graph[node]:
                    q.append((w+time, n))
        return max(t) if max(t) < float('inf') else -1
    
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        t = {}
        graph = collections.defaultdict(list)
        q = [(0, K)]
        for u, v, w in times:
            graph[u].append((v, w))
        while q:
            time, node = heapq.heappop(q)
            if node not in t:
                t[node] = time
                for n, w in graph[node]:
                    heapq.heappush(q, (w+time, n))
        return max(t.values()) if len(t) == N else -1

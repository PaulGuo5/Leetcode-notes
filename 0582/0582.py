class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(list)
        for i, j in zip(pid, ppid):
            graph[j].append(i)
        res = [kill]
        q = [kill]
        while q:
            node = q.pop()
            for i in graph[node]:
                res.append(i)
                q.append(i)
        return res

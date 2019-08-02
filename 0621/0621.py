class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt_tasks = {}
        for task in tasks:
            if task in cnt_tasks:
                cnt_tasks[task] += 1
            else:
                cnt_tasks[task] = 1
        max_val = max(cnt_tasks.values())
        p = 0
        for i in cnt_tasks.values():
            if i == max_val:
                p += 1
        return max(len(tasks), (n+1)*(max_val-1)+p)

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends or '0000' in deadends: return -1
        q = collections.deque([(0, '0000')])
        visited = set(['0000'])
        while q:
            val, node = q.popleft()
            if node not in deadends:
                if node == target:
                    return val
                children = []
                for i in range(len(node)):
                    children.append(node[:i]+str((int(node[i])+1)%10)+node[i+1:])
                    children.append(node[:i]+str((int(node[i])-1)%10)+node[i+1:])
                
                for child in children:
                    if child not in deadends and child not in visited:
                        visited.add(child)
                        q.append((val+1, child))
        return -1

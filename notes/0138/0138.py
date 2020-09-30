"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class CopyNode:
    def __init__(self, x = 0, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
        
class Solution:
    def copyRandomList1(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dic = collections.defaultdict(CopyNode)
        q = collections.deque([head])
        while q:
            cur = q.popleft()
            dic[cur].val = cur.val
            if cur.random:
                dic[cur.random].val = cur.random.val
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur.next].val = cur.next.val
                dic[cur].next = dic[cur.next]
                q.append(cur.next)
            else:
                break
            
        return dic[head]
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        dic = collections.defaultdict(Node)
        cur = head
        while cur:
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            nxt = dic.get(cur.next, None)
            rdm = dic.get(cur.random, None)
            dic[cur].next = nxt
            dic[cur].random = rdm
            cur = cur.next
        return dic[head]

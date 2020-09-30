class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None
        
class Skiplist:

    def __init__(self):
        self.S = [Node(None)]

    def search(self, target: int) -> bool:
        cur = self.S[-1]
        while cur:
            while cur.next and cur.next.val <= target:
                if cur.next.val == target:
                    return True
                cur = cur.next
            cur = cur.down
        return False
    
    def add(self, num: int) -> None:
        k = 1
        p = random.choice([0, 1])
        while p == 1 and k < len(self.S):
            k += 1
            p = random.choice([0, 1])
        if k == len(self.S):
            nr = Node(None)
            nr.down = self.S[-1]
            self.S.append(nr)
        cur = self.S[-1]
        kc = len(self.S)
        par = None
        while cur:
            while cur.next and cur.next.val <= num:
                cur = cur.next
            if kc <= k:
                nn = Node(num)
                nn.next = cur.next
                cur.next = nn
                if par:
                    par.down = nn
                par = nn
            cur = cur.down
            kc -= 1

    def erase(self, num: int) -> bool:
        cur = self.S[-1]
        res = False
        while cur:
            while cur.next and cur.next.val <= num:
                if cur.next.val == num:
                    res = True
                    cur.next = cur.next.next
                    break
                else:
                    cur = cur.next
            cur = cur.down
        while len(self.S) >= 2:
            cand = self.S[-2]
            if cand.next is None:
                self.S.pop()
            else:
                break
        return res


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)

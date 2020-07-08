class LRUCache1:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.od = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.od:
            self.od.move_to_end(key)
            return self.od[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od.move_to_end(key)
            self.od[key] = value
        else:
            if len(self.od) >= self.cap:
                self.od.popitem(last = False)
            self.od[key] = value
            
class Node:
    def __init__(self, k, val):
        self.k = k
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:
    def __init__(self, capacity:int):
        self.cap = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.table = {}
        
    def get(self, key):
        if key not in self.table:
            return -1
        else:
            node = self.table[key]
            self._delete(node)
            self._add(node)
            return node.val
        
    def put(self, key, val):
        if key in self.table:
            node = self.table[key]
            self._delete(node)
        new = Node(key, val)
        self._add(new)
        self.table[key] = new
        if len(self.table) > self.cap:
            node = self.head.next
            del self.table[node.k]
            self._delete(node)
            
            
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        self.tail.prev = node
        node.next = self.tail
        
    def _delete(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

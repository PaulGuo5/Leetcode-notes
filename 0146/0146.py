class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        # self.cache = collections.OrderedDict()
        self.cache = {}
        self.order = []
    def get(self, key: int) -> int:
        # if key in self.cache.keys():
        #     val = self.cache.pop(key)
        #     self.cache[key] = val
        #     return self.cache[key]
        # return -1
        if key in self.cache.keys():
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
    def put(self, key: int, value: int) -> None:
        # if key in self.cache:
        #     self.cache.pop(key)
        # elif len(self.cache) == self.cap:
        #     self.cache.popitem(last = False)
        # self.cache[key] = value
        if key in self.cache:
            self.order.remove(key)
        elif len(self.order) == self.cap:
                self.cache.pop(self.order.pop(0))
        self.order.append(key)
        self.cache[key] = value
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # self.hash_map = {}
        self.set = [None] * 1000000
        # self.set = [ None for i in range(1000000)]

    def add(self, key: int) -> None:
        # self.hash_map[key] = key
        self.set[key] = key

    def remove(self, key: int) -> None:
        # if key not in self.hash_map:
        #     return
        # del self.hash_map[key]
        self.set[key] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        # if key in self.hash_map:
        #     return True
        # return False
        if self.set[key] == None:
            return False
        return True
        # return self.set[key] != None
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

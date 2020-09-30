class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.hashmap = [[] for _ in range(self.buckets)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashkey = key % self.buckets
        key_pos = key // self.buckets
        
        if not self.hashmap[hashkey]:
            self.hashmap[hashkey] = [None]*self.buckets
        self.hashmap[hashkey][key_pos] = value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashkey = key % self.buckets
        key_pos = key // self.buckets
        if not self.hashmap[hashkey] or self.hashmap[hashkey][key_pos] == None:
            return -1
        return self.hashmap[hashkey][key_pos]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashkey = key % self.buckets
        key_pos = key // self.buckets
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][key_pos] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

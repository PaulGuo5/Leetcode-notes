class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.array = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.array.append(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        new = set()
        for n in self.array:
            if value - n in new:
                return True
            new.add(n)
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumOfDigits(i):
            return sum([int(d) for d in str(i)])
        
        table = collections.defaultdict(list)
        for i in range(1, n+1):
            table[sumOfDigits(i)].append(i)
        return len([i for i,j in table.items() if len(j)==max([len(x) for x in table.values()])])

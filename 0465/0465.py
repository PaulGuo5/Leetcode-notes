class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        if not transactions: return 0
        balance = collections.defaultdict(int)
        for t in transactions:
            balance[t[0]] = balance[t[0]] - t[2]
            balance[t[1]] = balance[t[1]] + t[2]
        balance_list = []
        for i, j in balance.items():
            if j != 0:
                balance_list.append(j)
        return self.helper(sorted(balance_list))
    
    def helper(self, balance):
        if len(balance) == 0: return 0
        min_trans = float("inf")
        for i in range(1, len(balance)):
            if balance[0]*balance[i] < 0:
                if balance[0]+balance[i] == 0:
                    min_trans = min(min_trans, self.helper(balance[1:i]+balance[i+1:])+1)
                else:
                    min_trans = min(min_trans, self.helper(balance[1:i]+balance[i+1:]+[balance[0]+balance[i]])+1)
        return min_trans

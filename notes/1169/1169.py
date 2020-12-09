class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = set()
        table = collections.defaultdict(set)
        for i, t in enumerate(transactions):
            tmp = t.split(",")
            name, time, amount, city = tmp[0], tmp[1], tmp[2], tmp[3]
            if int(amount) > 1000:
                res.add(t)
            for j in table[name]:
                if j[3] != city and abs(int(j[1])-int(time)) <= 60:
                    res.add(t)
                    res.add(j[0]+","+j[1]+","+j[2]+","+j[3])
            table[name].add((name, time, amount, city))
        return list(res)

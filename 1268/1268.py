class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, i, prefix = [], 0, ""
        for w in searchWord:
            prefix += w
            i =  bisect.bisect_left(products, prefix, i)
            tmp = []
            for p in products[i:i+3]:
                # if p.startswith(prefix):
                if p[:len(prefix)] == prefix:
                    tmp.append(p)
            res.append(tmp)
        return res

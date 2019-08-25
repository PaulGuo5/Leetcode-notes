class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = {}
        for domain in cpdomains:
            num = domain.split(" ")[0]
            url = domain.split(" ")[1]
            url_split = url.split(".")
            urls = []
            for i in range(len(url_split)):
                urls.append(".".join(url_split[i:]))
            for u in urls:
                if u not in dic:
                    dic[u] = int(num)
                else:
                    dic[u] += int(num)
        res = []
        for i, j in dic.items():
            res.append(str(j)+" "+i)
        return res

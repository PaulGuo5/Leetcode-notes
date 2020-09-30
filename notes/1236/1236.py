# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        domain = startUrl.split("http://")[1].split("/")[0]
        res = []
        q = collections.deque([startUrl])
        vis = set()
        while q:
            url = q.popleft()
            vis.add(url)
            res.append(url)
            for new in htmlParser.getUrls(url):
                sparsed_new = new.split("http://")[1].split("/")[0]
                if sparsed_new == domain:
                    if new not in vis:
                        vis.add(new)
                        q.append(new)
        return res

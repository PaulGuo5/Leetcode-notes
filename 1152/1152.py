class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        c = collections.defaultdict(list)
        for timestamp, username, website in sorted(zip(timestamp, username, website)):
            c[username].append(website)
        cnt = collections.Counter()
        for content in c.values():
            cnt += collections.Counter(set(itertools.combinations(content, 3)))
        return min(cnt, key = lambda x: (-cnt[x], x))

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        src = collections.defaultdict(set)
        ton = collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for i, j in zip(*pair):
                if i != j:
                    src[j].add(i)
                    ton[i].add(j)
                    break
        chars = set("".join(words))
        bfs = [n for n in chars if not src[n]]
        for i in bfs:
            for j in ton[i]:
                src[j].remove(i)
                if not src[j]:
                    bfs.append(j)
        return "".join(bfs) if len(bfs) == len(chars) else ""

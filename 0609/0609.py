class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for path in paths:
            root, contents = path.split()[0], path.split()[1:]
            for content in contents:
                file, name = content.split("(")
                res[name].append(root+'/'+file)
        return [file for file in res.values() if len(file) > 1]

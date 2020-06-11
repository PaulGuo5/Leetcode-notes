class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        email2name = {}
        for account in accounts:
            name, emails = account[0], account[1:]
            for email in emails:
                graph[emails[0]].add(email)
                graph[email].add(emails[0])
                email2name[email] = name
        visited = set()
        res = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                same_emails = []
                while stack:
                    e = stack.pop()
                    same_emails.append(e)
                    for nei in graph[e]:
                        if nei not in visited:
                            visited.add(nei)
                            stack.append(nei)
                res.append([email2name[email]]+sorted(same_emails))
        return res
                        
            

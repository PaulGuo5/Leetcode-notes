class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            emails[i] = emails[i].split("@")
            tmp = ""
            for char in emails[i][0]:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    tmp += char
            
            emails[i] = tmp + "@" + emails[i][1]
            tmp = ""
        emails = set(emails)
        return len(emails)

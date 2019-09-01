class Solution:
    def defangIPaddr1(self, address: str) -> str:
        return address.replace(".","[.]")
    
    
    def defangIPaddr(self, address: str) -> str:
        res = ""
        for i in address:
            if i ==".":
                res += "[.]"
            else:
                res += i
        return res

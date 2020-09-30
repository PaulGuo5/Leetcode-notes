class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validIPv4(str_):
            nums = str_.split(".")
            if len(nums) != 4:
                return False
            for n in nums:
                if not n or not n.isdecimal() or int(n) > 255 or int(n) < 0 or (n[0] == "0" and len(n) != 1):
                    return False
            return True
        
        def validIPv6(str_):
            valid16 = "0123456789abcdef"
            str_ = str_.lower()
            if "::" in str_:
                return False
            nums = str_.split(":")
            if len(nums) > 8:
                return False
            for n in nums:
                if len(n) > 4:
                    return False
                for i in n:
                    if i not in valid16:
                        return False
            return True
        
        if "." in IP and validIPv4(IP):
            return "IPv4"
        if ":" in IP and validIPv6(IP):
            return "IPv6"
        return "Neither"

class Codec:
        
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.string = ""
        for s in strs:
            self.string += str(len(s)) + " " + s
        return self.string

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = start = 0
        while i < len(s):
            if s[i] == " ":
                length = int(s[start: i])
                res.append(s[i+1: i+length+1])
                start = i+length+1
                i = start
            else:
                i += 1
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

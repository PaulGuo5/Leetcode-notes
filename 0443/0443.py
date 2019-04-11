class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        pre = chars[0]
        count = 0
        for char in chars:
            if char == pre:
                count += 1
            else:
                chars[index] = pre
                index += 1
                if count > 1:
                    for num in str(count):
                        chars[index] = num
                        index += 1
                pre = char
                count = 1
        chars[index] = char
        index += 1
        if count > 1:
                    for num in str(count):
                        chars[index] = num
                        index += 1
        return index

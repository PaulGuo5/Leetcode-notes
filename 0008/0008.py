class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        str = re.findall('(^[\+\-]?\d+)', str)
        print(str)
        try:
            result = int(''.join(str))
            MAX_INT = 2 ** 31 - 1
            MIN_INT = - 2 ** 31
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0

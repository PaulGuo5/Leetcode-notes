class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 != 0:
                res.append("Fizz")
            elif (i+1) % 5 == 0 and (i+1) % 3 != 0:
                res.append("Buzz")
            elif (i+1) % 5 == 0 and (i+1) % 3 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i+1))
        return res

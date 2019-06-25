from collections import Counter
class Solution:
    def getHint1(self, secret: str, guess: str) -> str:
        s, g = Counter(secret), Counter(guess)
        a = sum(i == j for i, j in zip(secret, guess))
        return "{}A{}B".format(a, sum((s & g).values()) - a)
    
    def getHint2(self, secret: str, guess: str) -> str:
        secret_count = {}
        guess_count = {}
        for char in secret:
            if char not in secret_count:
                secret_count[char] = 1
            else:
                secret_count[char] += 1
        for char in guess:
            if char not in guess_count:
                guess_count[char] = 1
            else:
                guess_count[char] += 1
        print(secret_count, guess_count)
        bulls_count = 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls_count += 1
        cows_count = 0
        for key in secret_count:
            if key in guess_count:
                cows_count += min(secret_count[key], guess_count[key])
        return "{}A{}B".format(bulls_count, cows_count - bulls_count)
    
    def getHint(self, secret: str, guess: str) -> str:
        secret_count = {}
        guess_count = {}
        bulls_count = 0
        cows_count = 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls_count += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1
        for key in secret_count:
            if key in guess_count:
                cows_count += min(secret_count[key], guess_count[key])
        return "{}A{}B".format(bulls_count, cows_count)

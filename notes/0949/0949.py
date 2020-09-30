class Solution:
    def largestTimeFromDigits1(self, A: List[int]) -> str:
        #does not work
        res = ""
        c = collections.Counter(map(str,A))
        for i in range(23, -1 ,-1):
            if i >= 10:
                if all(digit in c for digit in str(i)) and all(c[digit] != 0 for digit in str(i)):
                    res += str(i) + ":"
                    for digit in str(i):
                        c[digit] -= 1
                    break
            else:
                if all(digit in c for digit in "0"+str(i)) and all(c[digit] != 0 for digit in "0"+str(i)):
                    res += "0" + str(i) + ":"
                    for digit in str(i):
                        c[digit] -= 1
                    c["0"] -= 1
                    break
        for i in range(59, -1 ,-1):
            if i >= 10:
                if all(digit in c for digit in str(i)) and all(c[digit] != 0 for digit in str(i)):
                    res += str(i)
                    for digit in str(i):
                        c[digit] -= 1
                    break
            else:
                if all(digit in c for digit in "0"+str(i)) and all(c[digit] != 0 for digit in "0"+str(i)):
                    res += "0" + str(i)
                    for digit in str(i):
                        c[digit] -= 1
                    c["0"] -= 1
                    break
        return res
    
    
    def largestTimeFromDigits(self, A: List[int]) -> str:
        map_cnt = collections.Counter(map(str,A))
        for i in range(23, -1 ,-1):
            for j in range(59, -1, -1):
                if i >= 10 and j >= 10:
                    time = str(i) + str(j)
                elif i < 10 and j >= 10:
                    time = "0" + str(i) + str(j)
                elif i >= 10 and j < 10:
                    time = str(i) + "0" + str(j)
                else:
                    time = "0" + str(i) + "0" + str(j)
                map_time = collections.Counter(time)
                if map_time == map_cnt:
                    return time[:2]+":"+time[2:]
        return ""

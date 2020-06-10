class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1, date2=list(map(int,date1.split("-"))),list(map(int,date2.split("-")))
        lm = {1:True,3:True,5:True,7:True,8:True,10:True,12:True}
        def isleap(year):
            return True if (year%4==0 and year%100!=0) or year%400==0 else False
        def count_days(date):
            ans = 0
            for i in range(1971, date[0]):
                if isleap(i):
                    ans += 366
                else:
                    ans += 365
            for i in range(1, date[1]):
                if i == 2:
                    if isleap(date[0]):
                        ans += 29
                    else:
                        ans += 28
                elif i in lm:
                    ans+=31
                else:
                    ans+=30
            ans += date[2]
            return ans
        return abs(count_days(date1) - count_days(date2))

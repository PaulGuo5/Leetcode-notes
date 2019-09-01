class Solution:
    def dayOfYear(self, date: str) -> int:
        dic_ping = {"1":31, "2":28, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30, "01":31, "02":28, "03":31, "04":30, "05":31, "06":30, "07":31, "08":31, "09":30, "10":31, "11":30, "12":31}
        dic_run = {"1":31, "2":29, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30,"01":31, "02":29, "03":31, "04":30, "05":31, "06":30, "07":31, "08":31, "09":30, "10":31, "11":30, "12":31}
        year, month, date = date.split("-")[0], date.split("-")[1], date.split("-")[2]
        res = 0
        if ((int(year) % 4 == 0 and int(year) % 100 != 0) or (int(year) % 400 == 0 and int(year) % 3200 != 0)):
                if month == "01": 
                    return int(date)
                month_num = int(month)
                while month_num > 1:
                    month_num -= 1
                    res += dic_run[str(month_num)]
                res += int(date)
                return res
        else:
            if month == "01": 
                return int(date)
            month_num = int(month)
            while month_num > 1:
                month_num -= 1
                res += dic_ping[str(month_num)]
            res += int(date)
            return res

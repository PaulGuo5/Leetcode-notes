class Solution:
    # 计算1的个数
    def count_1(self,n):
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count
    
    def readBinaryWatch(self, num: int) -> List[str]:
        res=[]
        for hour in range(12):
            for minute in range(60):
                if self.count_1(hour)+self.count_1(minute) == num:
                    res.append("{0}:{1:02d}".format(hour, minute))
        return res
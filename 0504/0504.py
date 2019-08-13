class Solution:
    def convertToBase7v1(self, num: int) -> str:
        if num < 0:
            num_ = -num
        else:
            num_ = num
        res = ""
        while num_ >= 7:
            num_, r = divmod(num_, 7)
            res+=str(r)
        res+=str(num_)
        return res[::-1] if num >= 0 else "-"+res[::-1]
    
    def convertToBase7(self, num: int) -> str:
        if num < 0: return "-" + self.convertToBase7(-num)
        if num < 7: return str(num)
        return self.convertToBase7(num//7)  + str(num % 7)

class Solution:

    def __init__(self, w: List[int]):
        if not w:
            self.w_sum = []
        self.w_sum = [0]*len(w)
        self.w_sum[0] = w[0]
        for i in range(1, len(w)):
            self.w_sum[i] = self.w_sum[i-1] + w[i]
    
    def binarySearch(self, num):
        left, right = 0, len(self.w_sum)
        while left <= right:
            mid = (left+right)//2
            if self.w_sum[mid] == num:
                return mid
            if self.w_sum[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        return left
            

    def pickIndex(self) -> int:
        num = random.randint(1, self.w_sum[-1])
        return self.binarySearch(num)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

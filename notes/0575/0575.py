class Solution:
    def distributeCandies(self, candies: List[int]) -> int:   
        return min(len(collections.Counter(candies)), len(candies)//2)

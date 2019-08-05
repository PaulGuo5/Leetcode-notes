class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        cnt_candies = 0
        tmp = 1
        index = 0
        res = [0]*num_people
        while cnt_candies <= candies:
            if index == num_people:
                index = 0
            cnt_candies += tmp
            if cnt_candies >= candies:
                cnt_candies -= tmp
                res[index] += candies - cnt_candies
                break
            res[index] += tmp    
            index += 1
            tmp += 1
        return res
        

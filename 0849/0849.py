class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left, right = 0, len(seats)-1
        dis_left = 0
        dis_right = 0
        while seats[left] == 0:
            dis_left += 1
            left += 1
        while seats[right] == 0:
            dis_right += 1
            right -= 1
        dis = max(dis_left, dis_right)
        
        right = left + 1
        while right < len(seats):
            while seats[right] == 0 and right < len(seats)-1:
                right += 1
            temp_dis = right -left
            dis = max(dis, temp_dis // 2)
            left = right
            right += 1
        return dis
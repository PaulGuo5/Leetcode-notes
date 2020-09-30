class Solution:
    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point_index, point_red, point_blue = 0, 0, len(nums)-1
        while point_index <= point_blue:
            while nums[point_red] == 0 and point_red < point_blue:
                point_red += 1
            while nums[point_blue] == 2 and point_red < point_blue:
                point_blue -= 1
            if nums[point_index] == 2 and point_blue > point_index:
                nums[point_index], nums[point_blue] = nums[point_blue], nums[point_index]
                point_blue -= 1
            if nums[point_index] == 0 and point_red < point_index:
                nums[point_index], nums[point_red] = nums[point_red], nums[point_index]
                point_red += 1
            point_index += 1
            
    def sortColors(self, nums: List[int]) -> None:
        r, w, b = 0, 0, len(nums) - 1
        while w <= b:
            if nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
            elif nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            else:
                w += 1

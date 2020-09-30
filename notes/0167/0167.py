class Solution:
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            res = target - numbers[i]
            if res in dic:
                if i < dic[res]:
                    return [i+1, dic[res]+1]
                return [dic[res]+1, +1]
            else:
                dic[numbers[i]] = i
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        fst, lst = 0, len(numbers)-1
        while fst < lst:
            temp_sum = numbers[fst] + numbers[lst]
            if temp_sum == target:
                return [fst + 1, lst + 1]
            elif temp_sum < target:
                fst += 1
            elif temp_sum > target:
                lst -= 1
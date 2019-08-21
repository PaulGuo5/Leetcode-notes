class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # all indices will be stored here
        indices_dic = {}

        # add indices of all items to the dictionary
        for i, n in enumerate(nums):
            if n in indices_dic:
                indices_dic[n].append(i)
            else:
                indices_dic[n] = [i]

        # calculate the amount of the most frequent number
        M = max([len(i) for i in indices_dic.values()])

        # calculate length for all the most frequent numbers and get the shortest
        return min([i[-1]-i[0] for i in indices_dic.values() if len(i) == M]) + 1

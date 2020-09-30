from collections import Counter
class Solution:
    def findRestaurant2(self, list1: List[str], list2: List[str]) -> List[str]:
        # interest_list = list((Counter(list1) & Counter(list2)).elements())
        interest_list = set(list1) & set(list2)
        list1_map = {}
        list2_map = {}
        res = []
        for index in range(len(list1)):
            list1_map[list1[index]] = index
        for index in range(len(list2)):
            list2_map[list2[index]] = index
        interest_map = {}
        for interest in interest_list:
            interest_map[interest] = list1_map[interest] + list2_map[interest]
        for  key, value in interest_map.items():
            if value == min(interest_map.values()):
                res.append(key)
        return res
    
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        interest_list = set(list1) & set(list2)
        interest_map = Counter({v: i+1 for i, v in enumerate(list1) if v in interest_list}) + Counter({v: i+1 for i, v in enumerate(list2) if v in interest_list})
        res = min(interest_map.values())
        return [i for i, v in interest_map.items() if v == res]

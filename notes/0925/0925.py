class Solution:
    def isLongPressedName1(self, name: str, typed: str) -> bool:
        it = iter(typed)
        return all(char in it for char in name)
    
    
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #2 pointer
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i+=1
            elif j == 0 or typed[j-1] != typed[j]:
                return False
        return i == len(name)

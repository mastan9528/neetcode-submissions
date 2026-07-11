class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arr_1 = [0] * 26
        arr_2 = [0] * 26

        for s in s1:
            arr_1[ord(s)-ord('a')] +=1

        i = 0
        j= 0
        while j<len(s1):
            arr_2[ord(s2[j]) - ord('a')] +=1
            j +=1

        if arr_1 == arr_2:
            return True
        while j<len(s2):
            arr_2[ord(s2[i]) - ord('a')] -=1
            arr_2[ord(s2[j]) - ord('a')] +=1
            if arr_1 == arr_2:
                return True
            i +=1
            j +=1

        return False
    

            


        
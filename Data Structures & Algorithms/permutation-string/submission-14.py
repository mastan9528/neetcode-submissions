class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arr_1 = [0] * 26
        arr_2 = [0] * 26

        for i in range(len(s1)):
            arr_1[ord(s1[i])-ord('a')] +=1
            arr_2[ord(s2[i]) - ord('a')] +=1

        matches = 0
        for i in range(26):
            matches += (1 if arr_1[i] == arr_2[i] else 0)
        l = 0
        for r in range(len(s1) ,len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')

            arr_2[index] +=1
            if arr_1[index] == arr_2[index]:
                matches +=1
            elif arr_1[index]+1 == arr_2[index]:
                matches -=1

            index = ord(s2[l]) - ord('a')

            arr_2[index] -=1
            if arr_1[index] == arr_2[index]:
                matches +=1
            elif arr_1[index]-1 == arr_2[index]:
                matches -=1

            l +=1
        return matches == 26

            

             

    

            


        
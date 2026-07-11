class Solution:
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     if len(s1) > len(s2):
    #         return False

    #     dic = {}

    #     for i in range(len(s1)):
    #         dic[s1[i]] = 1 + dic.get(s1[i] , 0)

    #     i = 0 
    #     cnt = len(dic)
    #     dic1 = {}
    #     for j in range(len(s2)):

    #         if s2[j] in dic:
    #             dic1[s2[j]] = 1 + dic1.get(s2[j],0)
    #             if dic1[s2[j]] == dic[s2[j]]:
    #                 cnt -=1
    #             elif dic1[s2[j]] == dic[s2[j]]+1:
    #                 cnt +=1
    #                 while i < j and dic[s2[j]] != dic1[s2[j]]:
    #                     if s2[i] in dic:
    #                         dic1[s2[i]] -= 1
    #                         if dic1[s2[i]] == dic[s2[i]]:
    #                             cnt -= 1
    #                         elif dic1[s2[i]] < dic[s2[i]]:
    #                             cnt +=1
                            
    #                         if dic1[s2[i]] == 0:
    #                             del dic1[s2[i]]
    #                     i += 1

    #         if j-i+1 >len(s1):
    #             if s2[i] in dic1:
    #                 if s2[i] in dic and dic[s2[i]] == dic1[s2[i]]:
    #                     cnt +=1
    #                 dic1[s2[i]] -=1
    #                 if dic1[s2[i]] == 0:
    #                     del dic1[s2[i]]
    #             i +=1
    #         if cnt == 0 and j-i+1 == len(s1):
    #             return True

    #     return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Target frequencies
        dic = {}
        for char in s1:
            dic[char] = 1 + dic.get(char, 0)

        # cnt represents how many unique characters in s1 
        # currently have their frequency satisfied in the window
        dic1 = {}
        i = 0
        cnt = 0 
        target_matches = len(dic)

        for j in range(len(s2)):
            # 1. Add current character to window
            char_right = s2[j]
            if char_right in dic:
                dic1[char_right] = 1 + dic1.get(char_right, 0)
                if dic1[char_right] == dic[char_right]:
                    cnt += 1
                # If we just exceeded the count, this character no longer "matches" perfectly
                elif dic1[char_right] == dic[char_right] + 1:
                    cnt -= 1

            # 2. If window is too large, shrink from the left
            if j - i + 1 > len(s1):
                char_left = s2[i]
                if char_left in dic:
                    if dic1[char_left] == dic[char_left]:
                        cnt -= 1
                    dic1[char_left] -= 1
                    if dic1[char_left] == dic[char_left]:
                        cnt += 1
                i += 1

            # 3. Check if we have a perfect match
            if cnt == target_matches:
                return True

        return False
    

        
        


        
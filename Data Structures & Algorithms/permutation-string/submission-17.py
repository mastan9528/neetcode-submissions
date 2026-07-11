class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic_1 = {}
        dic = {}

        for ch in s1:
            dic_1[ch] = dic_1.get(ch , 0) + 1


        print(dic_1)

        cnt = len(dic_1)
        i , j = 0, 0
        while j < len(s2):

            if s2[j] not in dic_1:
                i = j+1
                j = j+1
                dic = {}
                cnt = len(dic_1)
                continue
            dic[s2[j]] = 1 + dic.get(s2[j] , 0)
            if dic[s2[j]] == dic_1[s2[j]]:
                cnt -=1
            elif dic[s2[j]] > dic_1[s2[j]]:
                while dic[s2[j]] > dic_1[s2[j]]:
                    if dic[s2[i]] == dic_1[s2[i]]:
                        cnt +=1
                    dic[s2[i]] -= 1
                    i +=1
            
            if cnt == 0:
                return True
            j +=1

            
        return False

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         dic_1 = {}
#         dic = {}

#         for ch in s1:
#             dic_1[ch] = dic_1.get(ch, 0) + 1

#         cnt = len(dic_1)
#         i, j = 0, 0
        
#         while j < len(s2):
#             # 1. Reset everything if character isn't in s1
#             if s2[j] not in dic_1:
#                 i = j + 1
#                 j = j + 1
#                 dic = {}
#                 cnt = len(dic_1)  # Fix 1: Reset cnt
#                 continue
            
#             # 2. Add current character to window
#             dic[s2[j]] = 1 + dic.get(s2[j], 0)
            
#             # 3. Update 'cnt' if we reached the target frequency
#             if dic[s2[j]] == dic_1[s2[j]]:
#                 cnt -= 1
            
#             # 4. If we have too many of s2[j], shrink from left until it's correct
#             elif dic[s2[j]] > dic_1[s2[j]]:
#                 while dic[s2[j]] > dic_1[s2[j]]:
#                     # If removing s2[i] breaks a perfect match, increment cnt
#                     if dic[s2[i]] == dic_1[s2[i]]:
#                         cnt += 1
#                     dic[s2[i]] -= 1
#                     i += 1
            
#             # 5. Final check for this window position
#             if cnt == 0: # Fix 2: Check at the end of the loop
#                 return True
                
#             j += 1

#         return False
        
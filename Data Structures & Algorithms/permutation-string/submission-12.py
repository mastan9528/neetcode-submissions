class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        dic = {}

        for i in range(len(s1)):
            dic[s1[i]] = 1 + dic.get(s1[i] , 0)

        i = 0 
        cnt = 0
        target = len(dic)
        dic1 = {}
        for j in range(len(s2)):

            if s2[j] in dic:
                dic1[s2[j]] = 1 + dic1.get(s2[j],0)
                if dic1[s2[j]] == dic[s2[j]]:
                    cnt +=1
                elif dic1[s2[j]] == dic[s2[j]]+1:
                    cnt -=1

            if j-i+1 >len(s1):
                if s2[i] in dic:
                    if dic[s2[i]] == dic1[s2[i]]:
                        cnt -=1
                    dic1[s2[i]] -=1
                    if dic1[s2[i]] == dic[s2[i]]:
                        cnt +=1
                i +=1
            if cnt == target:
                return True

        return False
    
    

        
        


        
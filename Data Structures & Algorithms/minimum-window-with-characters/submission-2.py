class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic_1 = {}
        dic = {}

        for ch in t:
            dic_1[ch] = dic_1.get(ch , 0) + 1


        print(dic_1)

        cnt = len(dic_1)
        i , j = 0, 0
        mini = 1001
        ans_len = 1001
        start = -1
        end = -1
        while j < len(s):
            if s[j] in dic_1:
                dic[s[j]] = 1+ dic.get(s[j],0)
                if dic[s[j]] == dic_1[s[j]]:
                    cnt -=1
            while cnt == 0:
                x = min(mini , j-i+1)
                if x < mini:
                    start = i
                    end = j+1
                    mini = x
                if s[i] in dic:
                    dic[s[i]] -=1
                    if dic[s[i]]+1 == dic_1[s[i]]:
                       cnt +=1
                i +=1

            
                # elif dic[s[j]] -1 == dic_1[s[j]]:
                #     cnt +=1
            j +=1

        return s[start:end] if start !=-1 and end != -1 else ""
             



        
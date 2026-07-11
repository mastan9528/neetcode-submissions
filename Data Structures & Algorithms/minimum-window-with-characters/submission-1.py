class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        dic = {}
        for val in t:
            dic[val] = 1+dic.get(val , 0)

        cnt = len(dic)
        mini = 10e9

        dic_2 = {}
        i , j = 0 , 0
        start = -1
        end = -1
        while j<len(s):
            if s[j] in dic:
                dic_2[s[j]] = 1+dic_2.get(s[j], 0)
                if dic_2[s[j]] == dic[s[j]]:
                    cnt -=1

            while i<=j and cnt == 0:
                x = min(mini , j-i+1)
                if x< mini:
                    start =i
                    end = j+1
                    mini =x
                if s[i] in dic_2:
                    dic_2[s[i]] -=1
                    if dic[s[i]] == dic_2[s[i]]+1:
                        cnt +=1
                        if dic_2[s[i]] == 0:
                            del dic_2[s[i]]

                i +=1
            j +=1
        return s[start:end] if start !=-1 and end != -1 else ""







        

        
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        dic = {}

        for ch in t:
            dic[ch] = 1 + dic.get(ch,0)
        cnt = len(dic)
        dic1 = {}
        mini = 10e9
        start = -1
        end = -1
        i = 0
        for j in range(len(s)):
            if s[j] in dic:
                dic1[s[j]] = 1 + dic1.get(s[j],0)
                if dic1[s[j]] == dic[s[j]]:
                    cnt -=1  
                
            while i<=j and cnt == 0:
                x = min(mini , j-i+1)
                if x < mini:
                    start = i
                    end =j+1
                    mini = x
                if s[i] in dic1:
                    dic1[s[i]] -=1
                    if dic1[s[i]] < dic[s[i]]:
                        cnt +=1
                        if dic1[s[i]]==0:
                            del dic1[s[i]]
                i +=1
        return s[start:end] if start != -1 and end != -1 else ""







        

        
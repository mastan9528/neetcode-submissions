from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            l = [0] * 26
            for x in s:
               l[ord(x)-ord('a')] += 1 
            v = tuple(l)
            dic[v].append(s)

        ls = []
        for values in dic.values():
            ls.append(values)

        return ls

        
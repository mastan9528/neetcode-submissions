from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            t = tuple(sorted(s))
            dic[t].append(s)

        return list(dic.values())
        

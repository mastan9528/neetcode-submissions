from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            t = tuple(sorted(s))
            dic[t].append(s)

        ls = []
        for val in dic.values():
            ls.append(val)
        return ls 
        

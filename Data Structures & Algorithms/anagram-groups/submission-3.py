from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            v = tuple(sorted(s))
            dic[v].append(s)

        ls = []
        for values in dic.values():
            ls.append(values)

        return ls

        
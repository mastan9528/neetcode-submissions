from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dic = defaultdict(list)
        for s in strs:
            arr = [0] * 26
            for i in range(len(s)):
                arr[ord(s[i]) - ord('a')] +=1

            dic[tuple(arr)].append(s)

        li = []

        for it in dic.values():
            li.append(it)

        return li


        
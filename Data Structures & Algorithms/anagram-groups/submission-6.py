class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for st in strs:
            arr = [0] *26
            for ch in st:
                arr[ord(ch)-ord('a')] +=1
            dic[tuple(arr)].append(st)
        result= []
        for key , value in dic.items():
            result.append(value)

        return result


            
        
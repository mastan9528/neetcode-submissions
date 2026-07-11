class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for i in nums:
            dic[i] +=1

        ls = []
        for ke , val in dic.items():
            ls.append([val ,ke])
        ls = sorted(ls , reverse = True)
        res = []
        i = 0
        while i < len(ls) and i < k :
            res.append(ls[i][1])
            i +=1
        return res
        

        
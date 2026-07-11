class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)

        for i in nums:
            dic[i] +=1

        ls = []
        for ke , val in dic.items():
            heapq.heappush(ls ,(val , ke))
            if len(ls) > k :
                heapq.heappop(ls)

        res = []
        for i in range(k):
            res.append(heapq.heappop(ls)[1])
        return res
        

        
        

        
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        maxi = 0
        for val in nums:
            dic[val] +=1
            maxi = max(maxi , dic[val])

        arr = [[] for i in range(maxi + 1)]

        for key , value in dic.items():
            arr[value].append(key)

        res=[]

        for i in range(len(arr)-1 , -1 , -1):
            for x in arr[i]:
                res.append(x)
                if len(res) == k:
                    return res

        return res

        


        
        
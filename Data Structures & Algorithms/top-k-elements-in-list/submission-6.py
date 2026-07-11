class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        li = []
        dic = defaultdict()
        maxi = 0
        for n in nums:
            dic[n] = 1 + dic.get(n , 0)
            maxi = max(maxi , dic[n])
        in_li = [[] for _ in range (len(nums)+1)]
        for key , value in dic.items():
            in_li[value].append(key)
        x= len(in_li)-1
        while x>0:
            if in_li[x] is not None:
               for val in in_li[x]:
                    if k == 0:
                        return li
                    li.append(val)
                    k -=1
            x -=1
        return li
                
        
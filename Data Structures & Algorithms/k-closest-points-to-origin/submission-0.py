import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []


        for i in range(len(points)):
            dis = math.sqrt((points[i][0]**2) + (points[i][1]**2))

            heapq.heappush(max_heap , [-dis , i])

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        ans = []
        while len(max_heap) >0:
            ind = max_heap[0][1]
            ans.append(points[ind])
            heapq.heappop(max_heap)

        return ans

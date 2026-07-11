class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i in range(k):
            heapq.heappush(heap , (-nums[i] , i))
        res = []
        res.append(-heap[0][0])
        for i in range(k , len(nums)):
            heapq.heappush(heap , (-nums[i] , i))
            while heap and heap[0][1] <i-k+1:
                heapq.heappop(heap)
            if heap:
                res.append(-heap[0][0])

        return res

        

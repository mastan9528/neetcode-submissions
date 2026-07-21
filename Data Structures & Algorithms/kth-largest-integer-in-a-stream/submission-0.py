class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.min_heap = []

        for i in range(len(nums)):
            heapq.heappush(self.min_heap , nums[i])

            if len(self.min_heap) > k :
                heapq.heappop(self.min_heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap , val)

        if len(self.min_heap) > self.k :
                heapq.heappop(self.min_heap)

        return self.min_heap[0]
        

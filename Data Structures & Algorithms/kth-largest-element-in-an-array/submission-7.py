import heapq
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     k = len(nums)-k
    #     def quickselect(l , r):
    #         pivot , p = nums[r] , l
    #         for i in range(l,r):
    #             if nums[i] <= pivot:
    #                 nums[i] , nums[p] = nums[p] , nums[i]
    #                 p +=1

    #         nums[p] ,nums[r] = nums[r] ,nums[p]


    #         if p>k : return quickselect(l , p-1)
    #         elif p<k: return quickselect(p+1,r)
    #         else:
    #             return nums[p]


    #     return quickselect(0 , len(nums)-1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap) # Removes the smallest of top k+1 elements
                
        return min_heap[0]



    

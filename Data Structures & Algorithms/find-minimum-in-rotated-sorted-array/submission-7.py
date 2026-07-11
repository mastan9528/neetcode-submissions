class Solution:
    def findMin(self, nums: List[int]) -> int:
        # i , j = 0 , len(nums)-1
        # mini = nums[0]
        # while i <= j:
        #     mid = ((j-i)//2) + i

        #     if nums[mid] >= nums[i]:
        #         mini =min(mini , nums[i])
        #         if nums[mid]<nums[j]: 
        #             j = mid -1
        #         else:
        #             i = mid+1
        #     else:
        #         mini = min(mini , nums[mid])
        #         j = mid -1
                

        # return mini
        low, high = 0, len(nums) - 1
    
        while low < high:
            mid = low + (high - low) // 2
            
            # If mid element is greater than the last element, 
            # the minimum must be in the right half.
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid)
            else:
                high = mid
                
        return nums[low]
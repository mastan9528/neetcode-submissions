class Solution:
    def findMin(self, nums: List[int]) -> int:
        i , j = 0 , len(nums)-1
        mini = 1001
        while i <= j:
            mid = ((j-i)//2) + i

            if nums[mid] >= nums[i]:
                mini =min(mini , nums[i])
                if nums[mid]<nums[j]: 
                    j = mid -1
                else:
                    i = mid+1
            else:
                mini = min(mini , nums[mid])
                j = mid -1
                

        return mini
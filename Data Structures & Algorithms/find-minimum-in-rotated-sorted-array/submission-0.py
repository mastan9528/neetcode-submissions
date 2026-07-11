class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        mini = 10e9
        while i<=j :
            mid = int((i+j)/2)
            if nums[i] <= nums[mid]:
                mini = min(mini,nums[i])
                i =mid+1
            else:
                mini = min(mini,nums[mid])
                j = mid-1
        return mini

        
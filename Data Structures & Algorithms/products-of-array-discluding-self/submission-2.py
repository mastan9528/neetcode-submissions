class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result_arr = [1] * len(nums)
        for i in range(1 , len(nums)):
            result_arr[i] = result_arr[i-1] * nums[i-1]
        product = 1
        for i in range(len(nums)-2 , -1 , -1):
            product *= nums[i+1] 
            result_arr[i] *= product 

        print(result_arr)
        return result_arr

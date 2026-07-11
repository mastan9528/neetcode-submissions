class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ls = []
        for i in range(len(nums)):
            if i > 0 and nums[i-1]==nums[i]:
                continue
            j , k  = i+1 , len(nums)-1
            while j < k:
                res = nums[i] + nums[j] + nums[k]
                if res == 0:
                    ls.append([nums[i],nums[j],nums[k]])
                    while j < k and nums[j+1] == nums[j]:
                        j +=1
                    while k > j and nums[k-1] == nums[k]:
                        k -=1
                    j +=1
                    k -=1
                elif res > 0:
                    k -=1
                else:
                    j +=1

        return ls
        
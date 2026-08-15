class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        vec_sum = 0
        def dfs(index , vec_sum):
            if index >= len(nums) or vec_sum >= target:
                if vec_sum == target:
                    res.append(subset.copy())
                return

            subset.append(nums[index])
            # print(subset)
            vec_sum += subset[-1]
            # print(vec_sum)
            dfs(index , vec_sum)
            vec_sum -= subset[-1]
            subset.pop()
            dfs(index+1 , vec_sum)

        dfs(0 , vec_sum) 
        return res

        
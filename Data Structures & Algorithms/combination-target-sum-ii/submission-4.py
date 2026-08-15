class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        candidates.sort()
        
        def dfs(index , subset , total):
            if index >= len(candidates) or total >= target:
                if total == target:
                    res.append(subset.copy())
                return

            for i in range(index , len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if total + candidates[i] > target:
                    return

                subset.append(candidates[i])
                dfs(i+1 , subset , total+candidates[i])
                subset.pop()
                
        dfs(0,[],0)

        return res
        
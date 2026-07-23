class Solution:
    def addi(self , li):
        s = 0
        for i in li:
            s += i

        return s

    def recursion(self , nums , index , target):

        if index >= len(nums) or self.addi(self.ans) >= target:
            if self.addi(self.ans) == target:
                self.ulti.append(list(self.ans))
            return

        self.recursion(nums , index+1, target)
        self.ans.append(nums[index])
        self.recursion(nums , index , target)
        self.ans.pop()
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.ulti = []
        self.recursion(nums , 0 ,target)

        return self.ulti


        
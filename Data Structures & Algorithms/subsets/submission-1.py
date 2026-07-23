class Solution:
    def recursion(self , nums , index):
        if index >= len(nums):
            self.ulti.append(list(self.ans))
            return

        self.recursion(nums , index+1)
        self.ans.append(nums[index])
        self.recursion(nums , index+1)
        self.ans.pop() 

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.ulti = []
        self.recursion(nums , 0)

        return self.ulti

        
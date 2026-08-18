class Solution:
    def recursion(self, nums ,index):
        if index >= len(nums):
            self.li.append(list(self.vec))
            return

        self.vec.append(nums[index])
        #print(self.vec)
        self.recursion(nums , index+1)
        self.vec.pop()
        while index + 1 < len(nums) and nums[index] == nums[index + 1]:
            index += 1
        self.recursion(nums , index+1)
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.li = []
        self.vec = []
        self.recursion(sorted(nums) , 0)

        return self.li
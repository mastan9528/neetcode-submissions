class Solution:

    def recursion(self, nums ,index):
        if index >= len(nums):
            self.li.append(list(self.vec))
            return


        self.vec.append(nums[index])
        #print(self.vec)
        self.recursion(nums , index+1)
        self.vec.pop()

        self.recursion(nums , index+1)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.li = []
        self.vec = []

        self.recursion(nums , 0)

        return self.li
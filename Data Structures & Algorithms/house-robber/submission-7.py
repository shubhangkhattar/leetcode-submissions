class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 2:
            return max(nums[0],nums[1])

        if len(nums) <= 2:
            return nums[0]
            

        n1 = nums[0]
        n2 = nums[1]

        for i in range(2,len(nums)):
            n1,n2 = max(n1,n2),max(n1+nums[i],n2)
        return n2



# [5,1,2,10,6,2,7,9,3,1]
#      i
# n1 = 1
# n2 = 1
# (5,10,2,9,1) 
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums):
            n1,n2 = 0,0

            for num in nums:
                n1,n2 = n2,max(n1+num,n2)
            
            return n2

        return max(nums[0],helper(nums[1:]),helper(nums[:-1]))
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        L = 0 
        R = 0 
        
        maxL,maxR = 0,0
        curr_sum = 0 
        max_sum = nums[0]

        for R in range(len(nums)):
            
            curr_sum += nums[R]

            if curr_sum < nums[R]:
                curr_sum = nums[R] 
                R = 0
                L = 0

            
            if curr_sum > max_sum:
                maxL = L
                maxR = R
                max_sum = curr_sum
            
        return max_sum
            



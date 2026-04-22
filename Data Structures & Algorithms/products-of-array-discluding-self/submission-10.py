class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,2,4,6]
        result = [1]*len(nums)
        pre = 1
        post = 1

        for i in range(len(nums)):

            result[i] = result[i]*pre
            result[len(nums)-i-1] = result[len(nums)-i-1]*post
            
            pre *= nums[i]
            post *= nums[len(nums)-i-1]
        
        return result

# pre - 1
# post - 1

# i = 0,1,2
# [1,2,4,6]
#        8
# 48  

# [48,24,12,8]
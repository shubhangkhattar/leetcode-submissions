class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = 1
        postfix = 1
        result = [1]*n

        for i in range(n):
            result[i] *= prefix
            prefix *= nums[i]

            result[n-i-1] *= postfix
            postfix *= nums[n-i-1]
        
        
        return result
        

    # [1,2,4,6]

    #  1,1,2,8
    # 48,24,6,1
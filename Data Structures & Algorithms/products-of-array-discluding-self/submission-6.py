class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix_array = [1]*n
        postfix_array = [1]*n
        prefix = 1
        postfix = 1

        for i in range(n):
            prefix_array[i] = prefix
            postfix_array[n-i-1] = postfix
            prefix *= nums[i]
            postfix *= nums[n-i-1]
        
        return [prefix_array[i] * postfix_array[i] for i in range(n)]
        


        


    # [1,2,4,6]

    #  1,1,2,8
    # 48,24,6,1
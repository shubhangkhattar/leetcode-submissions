class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        suffix = 1
        prefix_arr = []
        suffix_arr = []
        result = []
        n = len(nums)
        for i in range(n):
            prefix_arr.append(prefix)
            prefix *= nums[i]

        for i in range(n):
            suffix_arr.insert(0,suffix)
            suffix *= nums[n-i-1]

        for i in range(n):
            result.append(prefix_arr[i] * suffix_arr[i])
        
        return result
        
        
        

        





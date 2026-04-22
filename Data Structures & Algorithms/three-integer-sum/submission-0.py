class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []
        n = len(nums)
        results = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1 
            k = n - 1
            while j < k:
                
                inner_sum = nums[i] + nums[j] + nums[k]

                if inner_sum == 0:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                
                elif inner_sum < 0:
                    j += 1
                else:
                    k -= 1
            
        return result







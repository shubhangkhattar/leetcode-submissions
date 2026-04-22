class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        result = []

        i = 0 

        while i < len(nums):

            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue


            j = i + 1
            k = len(nums) - 1

            target = -1 * nums[i]

            while j < k:
                total = nums[j] + nums[k]

                if total == target:
                    result.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif total > target:
                    k-= 1
                else:
                    j += 1
            i += 1

        return result




        
        
        
        # -4,-1,-1,0,1,2
        #  0. 1. 2 3 4 5
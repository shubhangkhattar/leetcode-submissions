class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1

        result = float("inf")

        while l <= r:
            
            m = l + (r-l) // 2

            # Left sorted
            if nums[l] <= nums[m]:
                result = min(result,nums[l])
                l = m + 1
            else:
            # Right sorted
                result = min(result,nums[m])
                r = m - 1
        return result




        

        # [3,4,5,6,1,2]
        #  0 1 2 3 4 5
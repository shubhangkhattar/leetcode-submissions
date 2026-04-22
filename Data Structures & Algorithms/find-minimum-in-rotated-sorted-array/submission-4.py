class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = float("infinity")

        low = 0 
        high = len(nums) - 1

        while low <= high:

            if nums[low] <= nums[high]:
                return min(nums[low],min_val)
            
            mid = low + (high - low) //2
        
            if nums[low] <= nums[mid]:
                min_val = min(nums[low],min_val)
                low = mid + 1
            else:
                min_val = min(nums[mid],min_val)
                high = mid - 1

        return -1

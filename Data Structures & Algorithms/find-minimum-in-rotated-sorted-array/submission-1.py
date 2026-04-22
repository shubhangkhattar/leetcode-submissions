class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = float("infinity")

        low = 0 
        high = len(nums) - 1

        while low <= high:
            if nums[low] <= nums[high]:
                min_val = min(nums[low],min_val)
                return min_val
            
            mid = low + (high - low) //2
            min_val = min(nums[mid],min_val)

            if nums[low] <= nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return min_val

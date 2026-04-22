class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        min_val = float("infinity")
        sort_min = float("infinity")

        low = 0 
        high = len(nums) - 1

        while low <= high:
            
            mid = low + (high - low) //2

            min_val = min(nums[mid],min_val,sort_min)

            if nums[low] <= nums[mid]:
                sort_min = min(nums[low],sort_min)
                low = mid + 1
            else:
                high = mid - 1

        return min_val

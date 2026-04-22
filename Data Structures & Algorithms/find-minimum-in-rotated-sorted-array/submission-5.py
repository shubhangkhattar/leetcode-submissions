class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        right = n - 1

        min_sorted = nums[0]
        lowest = nums[0]

        while left <= right:

            mid = right + (right-right) // 2
            lowest = min(min_sorted,lowest,nums[mid])

            if nums[left] <= nums[mid]:
                min_sorted = nums[right]
                left = mid+1
            else:
                min_sorted = nums[left]
                right = mid-1
        
        return lowest

            



